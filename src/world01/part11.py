class loopSwitches:
    # switch 'break'
    for i in range(1, 15, 3):
        print(f"Current number: {i}")
        
        if (i >= 10):
            break
        """
        # output:
        Current number: 1
        Current number: 4
        Current number: 7
        Current number: 10
        """

    print("\n")

    # switch 'continue'
    for i in range(1, 15, 3):
        print(f"Current number: {i}")
        
        if (i >= 10):
            continue
        """
        # output:
        Current number: 1
        Current number: 4
        Current number: 7
        Current number: 10
        Current number: 13
        """

    print("\n")

    # switch 'pass'
    for i in range(1, 15, 3):
        print(f"Current number: {i}")
        
        if (i >= 10):
            pass
        """
        Current number: 1
        Current number: 4
        Current number: 7
        Current number: 10
        Current number: 13
        """
