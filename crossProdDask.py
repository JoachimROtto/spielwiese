import dask.array as da
import random
n = 10
a_in = [random.uniform(-100.0,100.0) for _ in range(3*n)]
b_in = [random.uniform(-100.0,100.0) for _ in range(3*n)]

# Zwei 3D-Vektoren als Dask Arrays
a = da.from_array(a_in, chunks=3)
b = da.from_array(b_in, chunks=3)

# Vektor-Kreuzprodukt berechnen
c = da.dot(a, b)
c.compute()