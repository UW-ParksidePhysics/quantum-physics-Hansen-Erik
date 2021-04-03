from numpy import *
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

N = 10
l = (N+1)**2/pi**2
t = 2*eye(N,)
u = -1*eye(N, N, -1)
v = -1*eye(N, N, 1)
w = t+u+v
matrix = l * w
eigvals, eigvecs = linalg.eig(matrix)
eigvals.sort()
print(eigvals[:5])
x1 = eigvecs[0]
x2 = eigvecs[1]
x3 = eigvecs[2]
plt.plot(eigvecs[0])
# plt.plot(n2)
# plt.plot(n3)
plt.show()  # this part doesnt seem correct, I assume it should look more uniform(sine-wave) and less pointed.

