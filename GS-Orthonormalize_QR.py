import numpy as np
from GS_Test import modifiedGramSchmidt

e1 = [1.0+1.0j, 1.0, 1.0j]  # Setting the values of the vectors(1d array)
e2 = [1.0j, 3.0, 1.0]
e3 = [0.0, 28.0, 8.0]

ep1 = e1/(np.linalg.norm(e1))  # |e1>/||e1|| Normalizing
w1 = np.vdot(ep1, e2)          # <e'1|e2>
v1 = ep1 * w1                  # <e'1|e2>|e'1>
u2 = np.subtract(e2, v1)       # |e2> - <e'1|e2>|e'1>
ep2 = u2/(np.linalg.norm(u2))  # Normalizing
w2 = np.vdot(ep1, e3)          # <e'1|e3>
v2 = ep1 * w2                  # <e'1|e3>|e'1>
w3 = np.vdot(ep2, e3)          # <e'2|e3>
v3 = w3 * ep2                  # <e'2|e3>|e'2>
u3 = np.subtract(e3, v2)       # |e3> - <e'1|e3>|e'1> - <e'2|e3>|e'2>
u4 = np.subtract(u3, v3)
ep3 = u4/(np.linalg.norm(u4))  # Normalizing

B = np.array([e1, e2, e3])  # Building matrix from the vector arrays
A = B.T  # Transposing the matrix, QR function looks for column vectors.
Q, R = np.linalg.qr(A, mode='complete')   # QR Decomposition; where Q is orthogonal unit vectors
M = -1 * Q.T  # Switching back to rows and inverting the sign

GS = (modifiedGramSchmidt(A))
gs_proof = GS.T

print()
print('Initial Vectors\n', B)
print('-------------------------------------------------------------')
print('Using the QR Method where Q = [|e1\'>], [|e2\'>], [|e3\'>]\n', M)
print('-------------------------------------------------------------')
print('Using the Modified_Gram-Schmidt Method_Pulled from internet_AuthorUnknown')
print(gs_proof)
print('-------------------------------------------------------------')
print('Done explicitly with GS method from Problem a.4')
print(ep1)
print(ep2)
print(ep3)
print('-------------------------------------------------------------')
print('Proof:\n dot product of |e1\'> & |e2\'> equals \n', np.vdot(ep1, ep2))
print('dot product of |e2\'> & |e3\'> equals \n', np.vdot(ep2, ep3))
print('dot product of |e1\'> & |e3\'> equals \n', np.vdot(ep1, ep3))
print('Norm of |e1\'> equals\n', np.linalg.norm(ep1))
print('Norm of |e2\'> equals\n', np.linalg.norm(ep2))
print('Norm of |e3\'> equals\n', np.linalg.norm(ep3))