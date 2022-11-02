import numpy as np
from sklearn import preprocessing

l = np.matrix('0 1 1 1 0; 1 0 0 1 0; 0 0 0 0 1; 0 1 1 0 0; 0 0 0 0 0')
lt = l.transpose()
h = np.matrix('1; 1; 1; 1; 1')

def compute(h):
    a = np.matmul(lt,h)
    a = preprocessing.minmax_scale(a, feature_range=(0, 1), axis=0, copy=True)
    return np.matmul(l,a)

for x in range(2):
    h = compute(h)