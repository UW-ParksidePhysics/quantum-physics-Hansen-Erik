import numpy as np

e1 = [1.0+1.0j, 1.0, 1.0j]  # Setting the values of the vectors(1d array)
e2 = [1.0j, 3.0, 1.0]
e3 = [0.0, 28.0, 8.0]

B = np.array([e1, e2, e3])  # Building matrix from the vector arrays
A = B.T  # Transposing the matrix, QR function looks for column vectors.
Q, R = np.linalg.qr(A, mode='complete')   # QR Decomposition; where Q is orthogonal unit vectors
M = -1 * Q.T  # Switching back to rows and inverting the sign

# I'll type out the math portion to show the steps for GS.
print()
print('Initial Vectors\n', B)
print('-------------------------------------------------------------')
print('Orthormal basis: Q = [|e1\'>], [|e2\'>], [|e3\'>]\n', M)
# print('-------------------------------------------------------------')
# print('Proof\n', O)
