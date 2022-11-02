import numpy as np
from sklearn.preprocessing import normalize

# Input web Matrix
l = np.matrix('0.0 1.0 1.0 1.0 0.0; 1.0 0.0 0.0 1.0 0.0; 0.0 0.0 0.0 0.0 1.0; 0.0 1.0 1.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0')

# Default matrices for calculation, do not alter
np.set_printoptions(precision=3)
lt = l.transpose()
h = np.matrix('1.0; 1.0; 1.0; 1.0; 1.0')
a = np.matrix('1.0; 1.0; 1.0; 1.0; 1.0')

# Computation for both hubiness and authority
def compute(h):
    a = np.matmul(lt,h)
    a *= np.matrix(1.0/a.max())
    h = np.matmul(l,a)
    h *= np.matrix(1.0/h.max())
    return a,h

# Iterate long enough for acceptable limits
for x in range(1000):
    a,h = compute(h)

# Print results
print("Hubiness:\n",h)
print("Authority:\n",a)