import numpy as np
import scipy.linalg

a1 = [1+1j, 1, 1j]  # Setting the values of the vectors(1d array)
a2 = [1j, 3, 1]
a3 = [0, 28, 8]

A = np.array([a1, a2, a3])  # Building matrix from the vector arrays

Q, R = scipy.linalg.qr(A)   # QR Decomposition; where Q is orthogonal unit vectors

# I'll add the steps that python is taking to get to Q(assuming it is correct.
# I haven't done the guided notes hand portion
# to figure out if my answer matches or if I need other steps.

print()
print('Initial Vectors\n', A)
print('-------------------------------------------------------------')
print('Q where Q = [[e1], [e2], [e3]\n', Q)
# print('-------------------------------------------------------------')
# print('R\n', R)
