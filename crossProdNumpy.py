import numpy as np

n = 1000000
a = np.random.rand(n, 3).astype(np.float32)
b = np.random.rand(n, 3).astype(np.float32)

c=  np.cross(a,b)