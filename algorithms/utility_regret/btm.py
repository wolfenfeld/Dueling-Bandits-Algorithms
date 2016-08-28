import numpy as np
from random import randint, random, choice
import math
from arms.single_bernoulli import SingleBernoulliArm
import copy


def myArgmin(A):
    # A is assumed to be a 1D array
    bottomInds = np.nonzero(A == A.min())[0]
    return bottomInds[randint(0, bottomInds.shape[0]-1)]


def myArgmax(A):
    # A is assumed to be a 1D array
    topInds = np.nonzero(A == A.max())[0]
    return topInds[randint(0, topInds.shape[0]-1)]


class BeatTheMean():

    def __init__(self, arms=list(), n_arms=0, initial_t=2**10):

        self.nArms = copy.copy(n_arms)  # Number of arms
        self.lArms = copy.copy(arms)      # Arms as a list of arms
        self.iArms = range(self.nArms)   # The indices of the arms
        self.dictArms = dict(zip(self.lArms, self.iArms))  # A dictionary
        self.numPlays = np.zeros([self.nArms, self.nArms])
        self.RealWins = np.zeros([self.nArms, self.nArms])
        self.gamma = 0.1
        self.delta = 1. / (2 * initial_t * self.nArms)
        self.t = 1
        self.firstPlace = 0

    def select_arms(self):
        # This returns two arms to compare.

        N = self.numPlays.sum(axis=1)
        self.firstPlace = myArgmin(N)
        index = randint(0, len(self.iArms)-1)
        secondPlace = self.iArms[index]

        return self.lArms[self.firstPlace], self.lArms[secondPlace], self.firstPlace, secondPlace

    def online_beat_the_mean(self):
        Wins = self.RealWins.sum(axis=1)
        N = self.numPlays.sum(axis=1)
        N = np.array([max(1, N[i]) for i in range(len(N))])
        P = Wins/N
        n = N.min()
        c = 3. * self.gamma * np.sqrt(math.log(1./self.delta)/n)

        if (P+c).min() <= (P-c).max():
            ind = myArgmin(P)
            newInds = sorted(list(set(range(self.nArms)) - set([ind])))
            self.nArms = self.nArms - 1
            self.lArms = [self.lArms[i] for i in newInds]
            self.iArms = range(self.nArms)
            self.dictArms = dict(zip(self.lArms, self.iArms))
            self.numPlays = self.numPlays[newInds][:, newInds]
            self.RealWins = self.RealWins[newInds][:, newInds]

    def update_scores(self, winner, loser, score=1):
        if winner == loser:
            score = float(random() < 0.5)

        if self.firstPlace == self.dictArms[winner]:
            first = self.dictArms[winner]
            second = self.dictArms[loser]
            self.RealWins[first, second] += score
            self.numPlays[first, second] += 1
        else:
            first = self.dictArms[loser]
            second = self.dictArms[winner]
            self.numPlays[first, second] += 1
        self.online_beat_the_mean()

        self.t += 1
        # return self.dictArms[winner]

    def update_delta(self, t):

        self.delta = self.delta = 1. / (2 * t**2 * self.nArms)

        return t**2


def run_btm_algorithm(n_arms, horizon, means):
    """ run_btm_algorithm() - This function runs the RUCB algorithm. """

    # Initializing the the average reward vector.
    average_reward = np.zeros(horizon)

    # Initializing the regret vector.
    regret = np.zeros(horizon)

    # Initializing the cumulative average reward vector.
    cumulative_average_reward = np.zeros(horizon)

    # Initializing the cumulative regret vector.
    cumulative_regret = np.zeros(horizon)

    arms = map(lambda (mu): SingleBernoulliArm(mu), means)

    initial_t = 2**10

    # Constructing the RUCB algorithm object.
    algorithm = BeatTheMean(arms=arms, n_arms=n_arms, initial_t=initial_t)

    for t in range(horizon):

        # Squaring trick.
        if t > initial_t:

            initial_t = algorithm.update_delta(t=t)

        # Selecting the arms.
        [chosen_left_arm, chosen_right_arm, chosen_left_arm_index, chosen_right_arm_index] = algorithm.select_arms()

        # Acquiring the rewards
        left_reward = chosen_left_arm.draw()

        right_reward = chosen_right_arm.draw()

        # Choosing the better arm.

        # Tie breaking rule.
        if left_reward == right_reward:

            if choice([True, False]):
                algorithm.update_scores(winner=chosen_left_arm, loser=chosen_right_arm, score=1)
            else:
                algorithm.update_scores(winner=chosen_right_arm, loser=chosen_left_arm, score=1)

        elif left_reward > right_reward:

            # Updating the wins matrix.
            algorithm.update_scores(winner=chosen_left_arm, loser=chosen_right_arm, score=1)

        else:
            # Updating the wins matrix.
            algorithm.update_scores(winner=chosen_right_arm, loser=chosen_left_arm, score=1)

        # Assigning the rewards and regrets.
        average_reward[t] = float(right_reward + left_reward) / (2+.0)

        regret[t] = max(means) - average_reward[t]

        if t == 1:
            cumulative_average_reward[t] = average_reward[t]

            cumulative_regret[t] = regret[t]
        else:
            cumulative_average_reward[t] = average_reward[t] + cumulative_average_reward[t-1]

            cumulative_regret[t] = regret[t] + cumulative_regret[t-1]

    # Returning the cumulative regret.
    return cumulative_regret


def run_several_iterations(iterations, arms, n_arms, horizon, means):
    """ run_several_iterations() - This function runs several iterations of the RUCB algorithm."""

    # Initializing the results vector.
    results = np.zeros(horizon)

    for iteration in range(iterations):

        # Adding the regret.
        results += run_btm_algorithm(n_arms, horizon, means)

    return results/(iterations + .0)

def run_several_iterations_and_save_results(algorithm, iterations, arms, n_arms, horizon, means, data_type):
    """ test_several_iterations() - This function runs several iterations of the Sparring algorithm. """

    # Initializing the results vector.
    result = np.zeros([horizon, iterations])

    file_name = "{0}_{1}_arms_{2}_horizon_{3}".format(algorithm, data_type, n_arms, horizon)

    for iteration in range(iterations):

        # The current cumulative regret.
        result[:, iteration] = run_btm_algorithm(n_arms, horizon, means)

    np.save(file_name, result)
