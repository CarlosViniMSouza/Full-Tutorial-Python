class nestedLoops:  
    rows = int(input("Insert number of rows: "))        # input -> 5
    columns = int(input("Insert number of columns: "))  # input -> 5

    for i in range(rows):
        for j in range(columns):
            print("$", end="")
        print()
    
    """
    # output:
    $$$$$
    $$$$$
    $$$$$
    $$$$$
    $$$$$
    """
