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
mat02 = np.array(
    [[2, 4, 5],
     [1, 0, -2],
     [3, -2, 1]]
)
```