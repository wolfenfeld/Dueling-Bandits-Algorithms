__author__ = 'wolfenfeld'
import numpy as np
# from tempfile import TemporaryFile
# temp_file = TemporaryFile()
k = 32
p_matrix_file_name = '/home/wolfenfeld/Studies/Dueling-Bandits-Algorithms/data/PMat.npy'
p_small_matrix_file_name = 'P_small_Mat.npy'
p_matrix = np.load(p_matrix_file_name)
smaller_p_matrix = p_matrix[1:k, 1:k]
with open(p_small_matrix_file_name, 'w') as f:
    np.save(f, smaller_p_matrix)

new_matrix = np.load('/home/wolfenfeld/Studies/Dueling-Bandits-Algorithms/data/P_small_Mat.npy')
print "yeah"