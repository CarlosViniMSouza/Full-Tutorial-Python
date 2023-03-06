# type casting -> convert the data for other type data!

class TypeCast:
    type01, type02 = 10, 8.5
    type03, type04 = "My Name", 'C'
    type05, type06 = True, "19"

    print(f"Type of var type04 = {type(type05)}")
    # output: Type of var type04 = <class 'bool'>

    print(f"Converting type01 for string = {type(str(type01))}")
    # output: Converting type01 for string = <class 'str'>

    print(f"Converting type06 for integer = {type(int(type06))}")
    # output: Converting type01 for string = <class 'int'>
