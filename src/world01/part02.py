class StringMethods:
    name = "CarlosViniMSouza"

    print(f"Length of variable = {len(name)}") 
    # output: 16

    print(f"Find one char = {name.find('C')}") # 0 -> found | -1 -> Not found

    print(f"Capitalized = {name.capitalize()}")
    # output: Carlosvinimsouza

    print(f"Is digit? = {name.isdigit()}")
    # output: False

    print(f"Replacing M by Z = {name.replace('M', 'Z')}")
    # output: CarlosViniZSouza
