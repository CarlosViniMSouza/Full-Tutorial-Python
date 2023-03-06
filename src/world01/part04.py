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
