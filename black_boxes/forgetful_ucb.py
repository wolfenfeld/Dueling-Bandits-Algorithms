import math
import numpy as np


class ForgetfulUCB():

    def __init__(self, counts, values, total_rewards):
        self.n_arms = 0
        self.counts = counts
        self.values = values
        self.total_rewards = total_rewards
        return
  
    def initialize(self, n_arms, p):
        self.n_arms = n_arms
        self.counts = np.zeros([n_arms, p+1])
        self.values = np.zeros(n_arms)
        self.total_rewards = np.zeros([n_arms, p+1])
        return
  
    def select_arm(self, p):

        for arm in range(self.n_arms):
            if self.counts[arm][p] == 0:
                return arm

        ucb_values = np.zeros(self.n_arms)
        if p != 0:
            total_counts = np.sum(self.counts[:, p-1:p+1])
        else:
            total_counts = np.sum(self.counts[:, p])

        for arm in range(self.n_arms):
            if p != 0:
                bonus = math.sqrt((0.25 * math.log(total_counts)) / float(np.sum(self.counts[arm, p-1:p+1])))
            else:
                bonus = math.sqrt((0.25 * math.log(total_counts)) / float(self.counts[arm, p]))

            ucb_values[arm] = self.values[arm] + bonus

        return np.argmax(ucb_values)

    def update(self, chosen_arm, reward, p):

        self.counts[chosen_arm, p] += 1

        self.total_rewards[chosen_arm, p] += reward
        if p != 0:
            self.values[chosen_arm] = \
                np.sum(self.total_rewards[chosen_arm, p-1:p+1]) / float(np.sum(self.counts[chosen_arm, p-1:p+1]))

        else:
            self.values[chosen_arm] = \
                self.total_rewards[chosen_arm, p] / float(self.counts[chosen_arm, p])

        return
