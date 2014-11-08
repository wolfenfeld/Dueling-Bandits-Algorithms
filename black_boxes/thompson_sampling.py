import random
import numpy as np


def ind_max(x):

    m = max(x)

    return x.index(m)


class UCB_TS():

    def __init__(self, values, successes, fails):

        self.successes = successes
        self.fails = fails
        self.values = values

        return
  
    def initialize(self, n_arms):

        self.successes = np.zeros(n_arms)
        self.fails = np.zeros(n_arms)
        self.values = np.zeros(n_arms)

        return
  
    def select_arm(self):

        for arm in range(len(self.successes)):
            self.values[arm] = random.betavariate(alpha=(self.successes[arm]+1), beta=(self.fails[arm]+1))

        return np.argmax(self.values)

    def update(self, chosen_arm, b_t):

        self.successes[chosen_arm] += b_t

        self.fails[chosen_arm] += (1-b_t)

        return
