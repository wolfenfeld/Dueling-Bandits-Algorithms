__author__ = 'wolfenfeld'
import numpy as np
NUMBER_OF_RANKERS = 64


def read_data(data_file_path):

    with open(data_file_path) as data_file:
        queri = 0
        data_lines = data_file.readlines()

        ranker_score = np.ndarray([data_lines.__len__(), NUMBER_OF_RANKERS])

        for line in data_lines:

            vector = line.split(' ')
            processed_vector = vector[2:-3]

            for i in xrange(64):
                ranker_score[queri][i] = float(processed_vector[i].split(':')[1])

            queri += 1

    return ranker_score

if __name__ == "__main__":
    path = "/home/wolfenfeld/Development/Dueling-Bandits/Data/NP2004/Fold1/test.txt"
    read_data(path)