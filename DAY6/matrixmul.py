import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

C = A @ B 
print("Matrix product C:")
print(C)

A_T = A.T
print("Transpose of A:")
print(A_T)

 M= np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 10]])
print("Square matrix M:")
print(M)


det_M = np.linalg.det(M)
print("Determinant of M:", det_M)

if det_M != 0:
    inv_M = np.linalg.inv(M)
    print("Inverse of M:")
    print(inv_M)
else:
    print("M is singular and has no inverse.")