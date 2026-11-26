import numpy as np

n = 1000000

a = np.random.uniform(low=-100.0, high=100.0, size=(3*n))
b = np.random.uniform(low=-100.0, high=100.0, size=(3*n))

c= [[] for _ in range(n)]
for i in range(0,3*-1,3):
    a_loc=[a[i], a[i+1], a[i+2]]
    b_loc=[b[i], b[i+1], b[i+2]]
    c[i] = np.cross(a_loc,b_loc)

