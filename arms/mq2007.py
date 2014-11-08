__author__ = 'wolfenfeld'
import numpy as np
NUMBER_OF_RANKERS = 46


class MQ2007Arms():

    def __init__(self, data_file_path):

        with open(data_file_path) as data_file:

            t = 0
            data_lines = data_file.readlines()

            self.ranker_score = np.ndarray([data_lines.__len__(), NUMBER_OF_RANKERS])

        for line in data_lines:

            split_line = line.split(' ')
            processed_line = split_line[2:2+NUMBER_OF_RANKERS]

            for i in xrange(NUMBER_OF_RANKERS):
                self.ranker_score[t][i] = float(processed_line[i].split(':')[1])

            t += 1

        self.means = np.mean(self.ranker_score, axis=0)

    def draw(self, arm, t):

        return self.ranker_score[t][arm]

if __name__ == "__main__":
    my_data_file_path = "/home/wolfenfeld/Development/Dueling-Bandits/Data/MQ2007/Fold1/train.txt"
    my_mq = MQ2007Arms(my_data_file_path)