import numpy as np

def encode_label(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

a = np.zeros((3, 1))
print(a)
