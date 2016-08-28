__author__ = 'wolfenfeld'
import numpy as np
import random
import os
MQ2007_NUMBER_OF_RANKERS = 46
NP2004_NUMBER_OF_RANKERS = 64
IMAT2009_NUMBER_OF_RANKERS = 127


class DataSet():

    def __init__(self, data_set_name):

        if data_set_name == "MQ2007":
            self.data_file_path = "/home/wolfenfeld/Studies/Dueling-Bandits-Algorithms/data/MQ2007/Fold1/test.txt"
            self.number_of_rankers = MQ2007_NUMBER_OF_RANKERS
        elif data_set_name == "NP2004":
            self.data_file_path = os.getcwd()+"/../data/NP2004/Fold1/train.txt"
            self.number_of_rankers = NP2004_NUMBER_OF_RANKERS
        elif data_set_name == "IMAT2009":
            self.data_file_path = os.getcwd()+"/../data/YandexLR/imat2009_learning.txt"
            self.number_of_rankers = IMAT2009_NUMBER_OF_RANKERS

        self.ranker_score = np.ndarray([])
        self.means = np.ndarray([])

    def set_data(self):
        with open(self.data_file_path) as data_file:

            t = 0
            data_lines = data_file.readlines()

            self.ranker_score = np.ndarray([data_lines.__len__(), self.number_of_rankers])

        for line in data_lines:

            split_line = line.split(' ')
            processed_line = split_line[2:2+self.number_of_rankers]

            for i in xrange(self.number_of_rankers):
                self.ranker_score[t][i] = float(processed_line[i].split(':')[1])

            t += 1

        self.means = np.mean(self.ranker_score, axis=0)

    def draw(self, left_arm, right_arm):

        query = random.randint(0, self.ranker_score.__len__()-1)

        random_left_variable = random.random()

        random_right_variable = random.random()

        if random_left_variable > self.ranker_score[query, left_arm]:
            left_reward = 0
        else:
            left_reward = 1

        if random_right_variable > self.ranker_score[query, right_arm]:
            right_reward = 0
        else:
            right_reward = 1

        return  [left_reward, right_reward]