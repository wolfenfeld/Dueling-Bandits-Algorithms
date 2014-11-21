import random
import numpy as np


class UCB_FTS():

    def __init__(self, values, successes, fails):
        self.n_arms = 0
        self.successes = successes
        self.fails = fails
        self.values = values

        return
  
    def initialize(self, n_arms, p):
        self.n_arms = n_arms
        self.successes = np.zeros([n_arms, p+1])
        self.fails = np.zeros([n_arms, p+1])
        self.values = np.zeros([n_arms, p+1])

        return
  
    def select_arm(self, p):

        for arm in range(self.n_arms):
            self.values[arm] = random.betavariate(alpha=(np.sum(self.successes[arm, p-1:p+1])+1),
                                                  beta=(np.sum(self.fails[arm, p-1:p+1])+1))

        return np.argmax(self.values[:, p])

    def update(self, chosen_arm, b_t, p):

        self.successes[chosen_arm, p] += b_t

        self.fails[chosen_arm, p] += (1-b_t)

        return
