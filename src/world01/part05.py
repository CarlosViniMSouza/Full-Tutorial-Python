import math


class MathFunctions:
    pi, num1, num2 = 3.141592, 6, 15

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
