# index operator -> [] : gives access to a sequence elements

class IndexingOperator:
    myName = "Carlos Souza"
    
    firstName = myName[:6].upper()
    lasName = myName[7:].lower()
    
    print(f"My name is: {firstName} {lasName}")

