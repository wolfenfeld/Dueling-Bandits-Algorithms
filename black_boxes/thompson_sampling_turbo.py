import random
import numpy as np
import math

def ind_max(x):

    m = max(x)

    return x.index(m)


class UCB_TS():

    def __init__(self, values, successes, fails, n_arms):

        self.n_arms = n_arms
        self.successes = successes
        self.fails = fails
        self.values = values

        return
  
    def initialize(self, n_arms):

        self.successes = np.zeros(n_arms)
        self.fails = np.zeros(n_arms)
        self.values = np.zeros(n_arms)

        return
  
    def select_arm(self, t):

        for arm in range(len(self.successes)):
            beta = self.fails[arm]+1 + math.log(1+t*pow(2, -t/(pow(self.n_arms, 2))))
            self.values[arm] = random.betavariate(
                alpha=(self.successes[arm] + 1
                       ),
                beta=beta
            )
        return np.argmax(self.values)

    def update(self, chosen_arm, b_t):

        self.successes[chosen_arm] += b_t

        self.fails[chosen_arm] += (1-b_t)

        return
