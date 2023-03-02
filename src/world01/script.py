## START of multiple assignment

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