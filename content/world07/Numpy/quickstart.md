## The Basics

NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes.

NumPy’s array class is called `ndarray`. It is also known by the alias `array`. Note that `numpy.array` is not the same as the Standard Python Library class `array.array`, which only handles one-dimensional arrays and offers less functionality. The more important attributes of a `ndarray` object are:

1. ndarray.ndim
2. ndarray.shape
3. ndarray.size
4. ndarray.dtype
5. ndarray.dtype
6. ndarray.itemsize
7. ndarray.data

See an example `(in app.py)`

## Array Creation

There are several ways to create arrays.

For example, you can create an array from a regular Python list or tuple using the `array` function. The type of the resulting array is deduced from the type of the elements in the sequences.

```python
matrix = np.array(
    [[2, 4, 5],
     [1, 0, -2],
     [3, -2, 1]]
)
```

## Printing Arrays

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:

° the last axis is printed from left to right,

° the second-to-last is printed from top to bottom,

° the rest are also printed from top to bottom, with each slice separated from the next by an empty line.
 
```python
matrix = np.arange(4) # one-dimensional
print(matrix)

matrix = np.arange(8).reshape(4, 2) # two-dimensional
print(matrix)

matrix = np.arange(30).reshape(3, 5, 2) # three-dimensional
print(matrix)
```

## Basic Operations

Unlike in many matrix languages, the product operator `*` operates elementwise in NumPy arrays. The matrix product can be performed using the `@` operator (in python >=3.5) or the `dot` function or method:

```python
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
```

Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.

```python
mat01 += mat02
print(mat01)

mat02 *= mat01
print(mat02)
```

By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by specifying the `axis` parameter you can apply an operation along the specified axis of an array:

```python

```