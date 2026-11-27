
# naiv: 1,2s
# numpy: 1,5s
# cupy: 2,1s
# jax/jit: 1,77
# numba mit cuda und numpy: 1,8
# numba mit cuda ohne numpy: (zickt bei result, typfehler?)
# numba mit cuda und cupy?: 2
# dask: timout bzw. 6s für 10.000(lazy ev, Ausführung bei result.compute())
import dask.array as da
import random
import numpy as np
n = 10000
a_in = [random.uniform(-100.0,100.0) for _ in range(3*n)]
b_in = [random.uniform(-100.0,100.0) for _ in range(3*n)]
a_in = [[1, 0,1], [0, 1,1]]

b_in = [[4, 1,5], [2, 2,1]]
#for i in range(0,3*n,3):
#    c[i]= a[i+1] * b[i+2] - a[i+2] * b[i+1]
#    c[i+1] = a[i+2] * b[i] - a[i] * b[i+2]
#    c[i+2] = a[i] * b[i+1] - a[i+1] * b[i]

