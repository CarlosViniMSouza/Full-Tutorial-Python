class FunctionsTest:
    def __init__(self):
        self.firstName = 'Carlos'
        self.lastName = 'Souza'
        self.age = 22
        
    def showHelloToUser(self):
        print(f"Hello {self.firstName} {self.lastName}\n")
        print(f"Your old age is {self.age}")
    
    def returnDoubleAge(self):
        return f"The old age duplicated is {self.age * 2}"

    def returnJob(self, info):
        return f"Your job is {info}"

    
people = FunctionsTest()

people.showHelloToUser()

print(people.returnDoubleAge())
print(people.returnJob("Software Engineer"))
