import numpy as np
a = [[1, 1, 1, 0, 0],
     [2, 2, 2, 0, 0],
     [1, 1, 1, 0, 0],
     [5, 5, 5, 0, 0],
     [0, 0, 0, 2, 2],
     [0, 0, 0, 3, 3],
     [0, 0, 0, 1, 1]]

[U, s, v] = np.linalg.svd(a)
S = np.diag(s)
V = v.T
print U
print S
print V
