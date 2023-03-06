class forLoops:
    myList = ['elem01', 'elem02', 'elem03']
    myString = "string!"

    for i in range(1, 10, 2):
        # range(start, end, increment)
        print(i, end=" ")
        # output: 1 3 5 7 9
    
    print("\n")
    
    for j in myList:
        print(j, end=" ")
        # output: elem01 elem02 elem03
    
    print("\n")

    for k in myString:
        print(k, end="")
        # output: string!
