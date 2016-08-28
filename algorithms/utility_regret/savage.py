import numpy as np
import math
import random


def arg_max(matrix):
    # A is assumed to be a 1D array
    top_indexes = np.nonzero(matrix == matrix.max())[0]
    return top_indexes[random.randint(0, top_indexes.shape[0]-1)]


def arg_min_2d(matrix):
    # A is assumed to be a 2D array
    m = matrix.min()
    r, c = np.nonzero(matrix == m)
    index = random.randint(0, r.shape[0]-1)
    return r[index], c[index]


def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))


def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))


def unique(a):
    """ return the list with duplicate elements removed """
    return list(set(a))


class SAVAGE():

    def __init__(self, arms=list(), n_arms=0, horizon=0):
        self.nArms = n_arms  # Number of arms
        self.lArms = arms       # Arms as a list of arms
        self.iArms = range(self.nArms)   # The indices of the arms
        self.numPlays = 2*np.ones([self.nArms, self.nArms])
        self.RealWins = np.ones([self.nArms, self.nArms])
        self.horizon = horizon
        self.delta = 1. / self.horizon
        self.t = 1
        self.PMat = self.RealWins / self.numPlays
        self.C = self.c(self.numPlays)
        self.C_plus_PMat = self.c(self.numPlays) + self.RealWins/self.numPlays
        self.firstPlace = 0
        self.secondPlace = 0
        self.activePairs = np.triu(np.ones([self.nArms, self.nArms]), 1)
        self.exploit = False
        self.champ = []
        self.chatty = False

    def c(self, N):
        return np.sqrt(math.log(0.0+self.nArms*(self.nArms-1)*self.horizon**2, 2)/(2*N))

    def indep_test(self):
        uI = list(np.nonzero(self.activePairs.any(axis=1))[0])
        uJ = list(np.nonzero(self.activePairs.any(axis=0))[0])
        indepArms = list(np.nonzero((self.C_plus_PMat > 0.5).sum(axis=1) < self.nArms)[0])
        newIndepArms = unique(intersect(indepArms, union(uI, uJ)))

        for i in newIndepArms:
            self.activePairs[i, :] = 0
            self.activePairs[:, i] = 0

    def stop_explore(self):
        I, J = np.nonzero(self.activePairs)
        if sum(I.shape) == 0:
            return True
        U_cop = (self.PMat > 0.5).sum(axis=1)
        bestArm = arg_max(U_cop)
        if U_cop[bestArm] == self.nArms-1 and (self.PMat[bestArm, :]-self.C[bestArm, :] > 0.5).sum() == self.nArms-1:
            return True

    def select_arms(self):
        # This returns two arms to compare.
        if self.exploit:
            if not self.champ:
                PMat = self.RealWins / self.numPlays
                self.champ = arg_max((PMat > 0.5).sum(axis=1))
            self.firstPlace = self.champ
            self.secondPlace = self.champ
        else:
            self.firstPlace, self.secondPlace = arg_min_2d(
                self.numPlays * self.activePairs + (self.activePairs == 0)*(self.numPlays.max()+1))

        return self.firstPlace, self.secondPlace

    def update_scores(self, winner, loser, score=1):

        # first = winner
        # second = loser
        if self.exploit:
            self.t += 1
            return
        self.RealWins[winner, loser] += score
        self.numPlays[winner, loser] += 1
        self.numPlays[loser, winner] += 1
        self.indep_test()
        if self.stop_explore():
            self.exploit = True
            self.numPlays = self.RealWins+self.RealWins.T
            PMat = self.RealWins / self.numPlays
            self.champ = arg_max((PMat > 0.5).sum(axis=1))
        self.t += 1
        self.C[winner, loser] = self.c(self.numPlays[winner, loser])
        self.PMat[winner, loser] = self.RealWins[winner, loser]/self.numPlays[winner, loser]
        self.C_plus_PMat[winner, loser] = self.C[winner, loser] + self.PMat[winner, loser]
        self.C[loser, winner] = self.c(self.numPlays[loser, winner])

        self.PMat[loser, winner] = self.RealWins[loser, winner] / self.numPlays[loser, winner]
        self.C_plus_PMat[loser, winner] = self.C[loser, winner] + self.PMat[loser, winner]
        return


def run_savage_algorithm(arms, n_arms, horizon, means):
    """ run_rcs_algorithm() - This function runs the RUCB algorithm. """

    # Initializing the the average reward vector.
    average_reward = np.zeros(horizon)

    # Initializing the regret vector.
    regret = np.zeros(horizon)

    # Initializing the cumulative average reward vector.
    cumulative_average_reward = np.zeros(horizon)

    # Initializing the cumulative regret vector.
    cumulative_regret = np.zeros(horizon)

    # Constructing the RUCB algorithm object.
    algorithm = SAVAGE(arms=arms, horizon=horizon, n_arms=n_arms)

    for t in range(horizon):

        # Selecting the arms.
        [chosen_left_arm, chosen_right_arm] = algorithm.select_arms()

        # Acquiring the rewards
        [left_reward, right_reward] = arms.draw(chosen_left_arm, chosen_right_arm)

        # Choosing the better arm.

        # Tie breaking rule.
        if left_reward == right_reward:

            if random.choice([True, False]):
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
        results += run_savage_algorithm(arms, n_arms, horizon, means)

    return results/(iterations + .0)

def run_several_iterations_and_save_results(algorithm, iterations, arms, n_arms, horizon, means, data_type):
    """ test_several_iterations() - This function runs several iterations of the Sparring algorithm. """

    # Initializing the results vector.
    result = np.zeros([horizon, iterations])

    file_name = "{0}_{1}_arms_{2}_horizon_{3}".format(algorithm, data_type, n_arms, horizon)

    for iteration in range(iterations):

        # The current cumulative regret.
        result[:, iteration] = run_savage_algorithm(arms, n_arms, horizon, means)

    np.save(file_name, result)



def test_functionality():

    a = np.random.randint(5, size=(3, 3))

    arg_min_2d(a)


if __name__ == "__main__":
    test_functionality()