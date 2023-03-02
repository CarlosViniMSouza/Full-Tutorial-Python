## START of multiple assignment

class MultipleAssignment:
    # way 1:
    name = "Carlos"
    age = 22
    status = True

    print(f"\nHy, I'm {name}, my age is {age}, and my student status is {status}")
    # output: Hy, I'm Carlos, my age is 22, and my student status is True

    # way 2:
    name, age, status = "Carlos Souza", 20, False

    print(f"Hy, I'm {name}, my age is {age}, and my student status is {status}")
    # output: Hy, I'm Carlos Souza, my age is 20, and my student status is False

## END of multiple assignment

## START of String Methods

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

## END of String Methods

## START of Type Cast

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

## END of Type Cast

## START of User Input