import numpy as np # hier reicht es durch cupy 
from numba import cuda

# Optionale Device-Funktion für bessere Lesbarkeit
@cuda.jit(device=True)
def cross_product_device(ax, ay, az, bx, by, bz):
    cx = ay * bz - az * by
    cy = az * bx - ax * bz
    cz = ax * by - ay * bx
    return cx, cy, cz

# CUDA-Kernel zur parallelen Berechnung über viele Vektoren
@cuda.jit
def cross_product_kernel(a, b, result):
    idx = cuda.grid(1)
    if idx < a.shape[0]:
        cx, cy, cz = cross_product_device(
            a[idx, 0], a[idx, 1], a[idx, 2],
            b[idx, 0], b[idx, 1], b[idx, 2]
        )
        result[idx, 0] = cx
        result[idx, 1] = cy
        result[idx, 2] = cz

# --- Anwendung ---
n = 1_000_000
a = np.random.rand(n, 3).astype(np.float32)
b = np.random.rand(n, 3).astype(np.float32)
result = np.empty_like(a)

# Speicher auf die GPU kopieren
d_a = cuda.to_device(a)
d_b = cuda.to_device(b)
d_result = cuda.device_array_like(result)

# Grid- und Block-Dimensionen festlegen
threads_per_block = 256
blocks_per_grid = (n + (threads_per_block - 1)) // threads_per_block

# Kernel starten
cross_product_kernel[blocks_per_grid, threads_per_block](d_a, d_b, d_result)

# Ergebnis zurück auf die CPU holen
result = d_result.copy_to_host()

# Kontrolle mit NumPy
#print("Ergebnis stimmt überein:", np.allclose(result, np.cross(a, b),rtol=0.1 ))
