from pyarma import *

A = mat(5, 5, fill.randu) # initialise 5x5 matrix with uniformly distributed random values
x = A[1,2]                # get element in row 1, column 2 (indices from 0)

M = umat(5, 5, fill.ones) # initialise unsigned integer matrix with ones
N = mat(M)                # convert to double-precision floating point

B = A + A                 # addition
C = A * B                 # matrix multiplication
D = A @ B                 # element-wise multiplication

X = cx_mat(A,B)           # initialise complex matrix with A as real, B as imaginary

# B.zeros()                 # fill B with zeros
# B.set_size(10,10)         # set size of B without preserving data
# B.ones(5,6)               # set size of B to 5x5, fill with ones

A.print()
B.print()
C.print()
D.print()             # print B with "B:" as header
