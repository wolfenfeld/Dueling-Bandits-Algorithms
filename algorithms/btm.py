import numpy as np
from random import randint, random, choice, sample
import math


def myArgmin(A, active_arms_indixes):
    # A is assumed to be a 1D array
    bottomInds = np.nonzero(A[active_arms_indixes] == A[active_arms_indixes].min())[0]
    return bottomInds[randint(0, bottomInds.shape[0]-1)]


def myArgmax(A):
    # A is assumed to be a 1D array
    topInds = np.nonzero(A == A.max())[0]
    return topInds[randint(0, topInds.shape[0]-1)]


class BeatTheMean():
    def __init__(self, arms=list(), n_arms=0, horizon=0):

        self.nArms = n_arms  # Number of arms
        self.initArms = arms
        self.iArms = range(self.nArms)   # The indices of the arms
        #taking arms to their indices.
        self.numPlays = np.zeros([self.nArms, self.nArms])
        self.RealWins = np.zeros([self.nArms, self.nArms])
        self.horizon = horizon
        self.gamma = 0.2
        self.delta = 1. / (2 * self.horizon * self.nArms)
        self.t = 1
        self.firstPlace = 0

    def select_arms(self):
        # This returns two arms to compare.
        N = self.numPlays.sum(axis=1)
        self.firstPlace = myArgmin(N, self.iArms)
        secondPlace = choice(self.iArms)
        return self.firstPlace, secondPlace

    def online_beat_the_mean(self):
        # wins = self.RealWins[self.iArms][:, self.iArms].sum(axis=1)
        # N = self.numPlays[self.iArms][:, self.iArms].sum(axis=1)
        wins = self.RealWins.sum(axis=1)
        N = self.numPlays.sum(axis=1)
        N = np.asarray([max(val, 1) for val in N])
        P = wins/N
        n = N[self.iArms].min()
        c = 3. * self.gamma * np.sqrt(math.log(1./self.delta)/n)

        if ((P+c)[self.iArms]).min() <= ((P-c)[self.iArms]).max():

            self.nArms -= 1
            self.iArms.remove(myArgmin(P, self.iArms))

    def update_scores(self, first, second, score=1):
        if first == second:
            score = float(random() < 0.5)

        if self.firstPlace == first:

            self.RealWins[first, second] += score
            self.numPlays[first, second] += 1
        else:
            self.numPlays[second, first] += 1
        self.online_beat_the_mean()

        self.t += 1


def run_btm_algorithm(arms, n_arms, horizon, means):
    """ run_btm_algorithm() - This function runs the RUCB algorithm. """

    # Initializing the the average reward vector.
    average_reward = np.zeros(horizon)

    # Initializing the regret vector.
    regret = np.zeros(horizon)

    # Initializing the cumulative average reward vector.
    cumulative_average_reward = np.zeros(horizon)

    # Initializing the cumulative regret vector.
    cumulative_regret = np.zeros(horizon)

    # Constructing the RUCB algorithm object.
    algorithm = BeatTheMean(arms=arms, horizon=horizon, n_arms=n_arms)

    for t in range(horizon):

        # Selecting the arms.
        [chosen_left_arm, chosen_right_arm] = algorithm.select_arms()

        # Acquiring the rewards
        [left_reward, right_reward] = arms.draw(chosen_left_arm, chosen_right_arm)

        # Choosing the better arm.

        # Tie breaking rule.
        if left_reward == right_reward:

            if choice([True, False]):
                algorithm.update_scores(chosen_left_arm, chosen_right_arm)
            else:
                algorithm.update_scores(chosen_right_arm, chosen_left_arm)

        elif left_reward > right_reward:

            # Updating the wins matrix.
            algorithm.update_scores(chosen_left_arm, chosen_right_arm)

        else:
            # Updating the wins matrix.
            algorithm.update_scores(chosen_right_arm, chosen_left_arm)

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
        results += run_btm_algorithm(arms, n_arms, horizon, means)

    return results/(iterations + .0)