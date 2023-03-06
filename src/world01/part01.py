class MultipleAssignment:
    # way 1:
    name = "Carlos"
    age = 22
    status = True

    print(f"Hy, I'm {name}, my old age is {age}, and my student status is {status}")
    # output: Hy, I'm Carlos, my age is 22, and my student status is True

    # way 2:
    name, age, status = "Carlos Souza", 20, False

    print(f"Hy, I'm {name}, my old age is {age}, and my student status is {status}")
    # output: Hy, I'm Carlos Souza, my age is 20, and my student status is False
