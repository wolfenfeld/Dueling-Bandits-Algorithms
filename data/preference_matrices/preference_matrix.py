__author__ = 'wolfenfeld'
import numpy as np
import random


class PreferenceMatrix():
    def __init__(self):
        self.p_values = None
        self.condorcet_winner = None
        self.n_arms = None
        self.delta = None

    def init(self, p_mat_file_name):

        self.p_values = np.load(p_mat_file_name)

        self.n_arms = self.p_values.shape[0]

        self.set_condorcet_winner()

        self.set_delta()

    def set_condorcet_winner(self):
        for i in range(self.n_arms):

            row = [value > 0.5 for value in self.p_values[i, :]]
            row[i] = True
            if all(row):
                self.condorcet_winner = i

    def set_delta(self):

        self.delta = np.zeros(self.n_arms)

        for i in range(self.n_arms):
            self.delta[i] = self.p_values[self.condorcet_winner, i] - 0.5

    def draw(self, left_arm, right_arm):

        p_value = self.p_values[left_arm, right_arm]

        random_variable = random.random()

        if random_variable > p_value:
            return [0, 1]
        else:
            return [1, 0]

    def get_regret(self, left_arm, right_arm):

        return (self.delta[left_arm] + self.delta[right_arm]) / 2.0

if __name__ == "__main__":
    my_p_mat = PreferenceMatrix()
    my_p_mat.init('BvsC20.npy')

    print('yeah')