__author__ = 'wolfenfeld'
import random


class BernoulliArms():

    def __init__(self, means):

        self.means = means

    def draw(self, left_arm, right_arm):

        random_left_variable = random.random()

        random_right_variable = random.random()

        if random_left_variable > self.means[left_arm]:
            left_reward = 0
        else:
            left_reward = 1

        if random_right_variable > self.means[right_arm]:
            right_reward = 0
        else:
            right_reward = 1

        return [left_reward, right_reward]