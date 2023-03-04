## START of multiple assignment ##

class MultipleAssignment:
    # way 1:
    name = "Carlos"
    age = 22
    status = True

    print(f"\nHy, I'm {name}, my old age is {age}, and my student status is {status}")
    # output: Hy, I'm Carlos, my age is 22, and my student status is True

    # way 2:
    name, age, status = "Carlos Souza", 20, False

    print(f"Hy, I'm {name}, my old age is {age}, and my student status is {status}")
    # output: Hy, I'm Carlos Souza, my age is 20, and my student status is False

## END of multiple assignment ##

## START of String Methods ##

class StringMethods:
    name = "CarlosViniMSouza"

    print(f"\nLength of variable = {len(name)}") 
    # output: 16

    print(f"Find one char = {name.find('C')}") # 0 -> found | -1 -> Not found

    print(f"Capitalized = {name.capitalize()}")
    # output: Carlosvinimsouza

    print(f"Is digit? = {name.isdigit()}")
    # output: False

    print(f"Replacing M by Z = {name.replace('M', 'Z')}")
    # output: CarlosViniZSouza

## END of String Methods ##

## START of Type Cast ##

# type casting -> convert the data for other type data!

class TypeCast:
    type01, type02 = 10, 8.5
    type03, type04 = "My Name", 'C'
    type05, type06 = True, "19"

    print(f"\nType of var type04 = {type(type05)}")
    # output: Type of var type04 = <class 'bool'>

    print(f"Converting type01 for string = {type(str(type01))}")
    # output: Converting type01 for string = <class 'str'>

    print(f"Converting type06 for integer = {type(int(type06))}")
    # output: Converting type01 for string = <class 'int'>

## END of Type Cast ##

## START of User Input ##

"""
WARNING: ALL and any data inserted in typing how to string!!
        You should do type cast if need a specific type data
        It can be so mush necessary in some situations
"""

class UserInput:
    # Example for convert 'str' in 'float'
    salary = float(input("\nMy salary: "))

    # print("The salary is " + salary)
    # --> TypeError: can only concatenate str (not "float") to str

    # To make it work, use 'str()'

    print("The salary is " + str(salary))
    # output: The salary is 1443.2

    print(f"The salary is a variable of type {type(salary)}")
    # output: The salary is a variable of type <class 'float'>

## START of Math Functions
import math

class mathFunctions:
    pi = 3.141592
    num1 = 6
    num2 = 15

    print("\n")

    print(round(pi)) 
    # output: 3
    print(math.ceil(pi))
    # output: 4
    print(math.floor(pi))
    # output: 3

    print(abs(pi))
    # output: 3.141592
    print(pow(pi, 3))
    # output: 31.006257328285752

    print(math.sqrt(num2))
    # output: 3.872983346207417

    print(max(pi, num1, num2))
    # output: 15
    print(min(pi, num1, num2))
    # output: 3.141592

## END of Math Functions

## START of string slicing
"""
Create a substring by a string exist;
Two forms: 
    1. indexing -> [start:stop:step]
    2. slice() -> slice(start:stop:step)
"""

class stringSlicing:
    myString = "This is a string for test!"

    print("\n")

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

## END of string slicing

## START of IF Statement

class ifStatement:
    choose = "student" # 'student', or 'proof', or 'collaborator'

    if (choose == "student"):
        print("\nYou are a student")
    elif (choose == "proof"):
        print("\nYou are a proof")
    elif (choose == "collaborator"):
        print("\nYou are a collaborator")
    else:
        print("Error!")

    # output: You are a student

## END of IF Statement

## START of while loops

class whileLoops:
    count = 4

    print("\n")

    while (count > 0):
        print(f"Your value count: {count}")
        count -= 1
    
    #  output:
    # Your value count: 4
    # Your value count: 3
    # Your value count: 2
    # Your value count: 1

## END of while loops

## START of For loops

class forLoops:
    myList = ['elem01', 'elem02', 'elem03']
    myString = "string!"

    print("\n")

    for i in range(1, 10, 2):
        # range(start, end, increment)
        print(i, end=" ")

    # output: 1 3 5 7 9
    print("\n")
    
    for j in myList:
        print(j, end=" ")

    # output: elem01 elem02 elem03
    print("\n")

    for k in myString:
        print(k, end="")
    
    # output: string!

## END of For loops

## START of nested loops

class nestedLoops:
    rows = int(input("\nInsert number of rows: ")) # input -> 5
    columns = int(input("Insert number of columns: ")) # input -> 5

    for i in range(rows):
        for j in range(columns):
            print("$", end="")
        print()
    
    """
    # output:
    $$$$$
    $$$$$
    $$$$$
    $$$$$
    $$$$$
    """

## END of nested loops

## START of loops Switches

class loopSwitches:
    print("\n")

    # switch 'break'
    for i in range(1, 15, 3):
        print(f"Current number: {i}")
        
        if (i >= 10):
            break
    """
    # output:
    Current number: 1
    Current number: 4
    Current number: 7
    Current number: 10
    """

    print("\n")

    # switch 'continue'
    for i in range(1, 15, 3):
        print(f"Current number: {i}")
        
        if (i >= 10):
            continue
    """
    # output:
    Current number: 1
    Current number: 4
    Current number: 7
    Current number: 10
    Current number: 13
    """

    print("\n")

    # switch 'pass'
    for i in range(1, 15, 3):
        print(f"Current number: {i}")
        
        if (i >= 10):
            pass
    """
    Current number: 1
    Current number: 4
    Current number: 7
    Current number: 10
    Current number: 13
    """

## END of loops Switches
