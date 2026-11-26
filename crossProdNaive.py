import random

n = 1000000
a = [random.uniform(-100.0,100.0) for _ in range(3*n)]
b = [random.uniform(-100.0,100.0) for _ in range(3*n)]
c= [0 for _ in range(3*n)]

for i in range(0,3*n,3):
    c[i]= a[i+1] * b[i+2] - a[i+2] * b[i+1]
    c[i+1] = a[i+2] * b[i] - a[i] * b[i+2]
    c[i+2] = a[i] * b[i+1] - a[i+1] * b[i]