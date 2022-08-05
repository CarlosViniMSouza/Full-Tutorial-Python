import numpy as np

mat01 = np.arange(16).reshape(4, 4)

print("Our matrix: \n", mat01)

print("The shape: ", mat01.shape)
print("Dimensions: ", mat01.ndim)
print("Size of each element: ", mat01.itemsize)
print("Type matrix: ", type(mat01))

# Array Creation #

mat02 = np.array(
    [[2, 4, 5],
     [1, 0, -2],
     [3, -2, 1]]
)

print("\nThe Matrix 02: \n", mat02)
print("Scale Matrix 02: ", mat02.size)

# Printing Arrays #

mat03 = np.arange(4) # one-dimensional
print(mat03)

mat03 = np.arange(8).reshape(4, 2) # two-dimensional
print(mat03)

mat03 = np.arange(30).reshape(3, 5, 2) # three-dimensional
print(mat03)
