import random
# naiv: 1,2s
# numpy: 1,7s
# cupy: 2,1s
# jax/jit: 1,77
# numba ohne cuda:
# numba mit cuda
# numba mit numpy/cupy?
# dask


#n = 1000000
#a = [random.uniform(-100.0,100.0) for _ in range(3*n)]
#b = [random.uniform(-100.0,100.0) for _ in range(3*n)]
#c= [0 for _ in range(3*n)]

#for i in range(0,3*n,3):
#    c[i]= a[i+1] * b[i+2] - a[i+2] * b[i+1]
#    c[i+1] = a[i+2] * b[i] - a[i] * b[i+2]
#    c[i+2] = a[i] * b[i+1] - a[i+1] * b[i]

import jax.numpy as jnp
import jax
@jax.jit
def main():
    n = 1000000
    key=jax.random.key(42)
    a = jax.random.uniform(key, shape=(3*n), dtype=jnp.float32)
    b = jax.random.uniform(key, shape=(3*n), dtype=jnp.float32)
    c= [[] for _ in range(n)]
    for i in range(0,3*-1,3):
        a_loc=[a[i], a[i+1], a[i+2]]
        b_loc=[b[i], b[i+1], b[i+2]]
        c[i] = jnp.cross(a_loc,b_loc)

print(jax.default_backend())
print(jax.devices())
#Status: das läuft gut aber python -c "import jax; print(jax.devices())" sagt dass es devices geben kann aber der Versionskonflikt eine Fallback erzwingt. 
# Warum ist das im Debuzgging nicht so?