"""
Create a substring by a string exist;
Two forms: 
    1. indexing -> [start:stop:step]
    2. slice() -> slice(start:stop:step)
"""

class StringSlicing:
    myString = "This is a string for test!"

    print(myString[0:4])
    # output: This

    print(myString[5:]) # [5:end]
    # output: is a string for test!

    print(myString[::2]) # [0:end:2]
    # output: Ti sasrn o et

    print(myString[::-1]) # [0:end:-1]
    # output: !tset rof gnirts a si sihT

    myStringSlice = slice(5, 16, 1)

    print(myString[myStringSlice])
    # output: is a string
