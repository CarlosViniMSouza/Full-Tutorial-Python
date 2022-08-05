import numpy as np

matrix = np.arange(16).reshape(4, 4)

print("Our matrix: \n", matrix)

print("The shape: ", matrix.shape)
print("Dimensions: ", matrix.ndim)
print("Size of each element: ", matrix.itemsize)
print("Type matrix: ", type(matrix))

# Array Creation #

matrix = np.array(
    [[2, 4, 5],
     [1, 0, -2],
     [3, -2, 1]]
)

print("\nThe Matrix 02: \n", matrix)
print("Scale Matrix 02: ", matrix.size)

# Printing Arrays #

matrix = np.arange(4) # one-dimensional
print(matrix)

matrix = np.arange(8).reshape(4, 2) # two-dimensional
print(matrix)

matrix = np.arange(30).reshape(3, 5, 2) # three-dimensional
print(matrix)

mat01 = np.array([
    [5, 4],
    [3, 6]
])

mat02 = np.array([
    [0, 1],
    [2, -1]
])

print(mat01 * mat02, "\n") # elementwise product
print(mat01 @ mat02, "\n") # matrix product (as we know)
print(mat01.dot(mat02), "\n") # another way matrix product

mat01 += mat02
print(mat01)

mat02 *= mat01
print(mat02)

matrix = np.arange(16).reshape(4, 4)

print("\nSum elements by column: \n", matrix.sum(axis=0))
print("\nSum elements by row: \n", matrix.sum(axis=1))
print("\nAcumulated sum in each row: \n", matrix.cumsum(axis=1))