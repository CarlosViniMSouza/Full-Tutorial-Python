"""
Nested Functions Calls -> function calls inside other functions calls ...
                            innermost function calls are resolved first ...
                            returned values is used as argument for next function call.
"""

class NestedFunctionsCalls:
    def calculateLiquidSalary() -> None:
        liquidSalary = round(abs(float(input("Enter your brute salary: "))))

        print(f"Remainder is: US${liquidSalary - (liquidSalary * 0.15)}")
    
    calculateLiquidSalary()
