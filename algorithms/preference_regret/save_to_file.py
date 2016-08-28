__author__ = 'wolfenfeld'
import numpy as np

with open('test123', 'w') as f:

    test = np.zeros([2, 4])
    test[1, 2] = 1
    np.save(f.name, test)


b = np.load('test123.npy')

print b