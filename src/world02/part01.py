class Lists:
    myFoodList = ['pizza', 'hamburger', 'hot-dog', 'pudding']

    print(myFoodList[1])
    # output: 'hamburger'

    # Methods for handle lists:

    myFoodList.append('cheese-burger')
    print(myFoodList)
    # output: ['pizza', 'hamburger', 'hot-dog', 'pudding', 'cheese-burger']

    myFoodList.remove('hot-dog')
    print(myFoodList)
    # output: ['pizza', 'hamburger', 'pudding', 'cheese-burger']
    
    myFoodList.insert(0, 'cake strawberries')
    print(myFoodList)
    # output: ['cake strawberries', 'pizza', 'hamburger', 'pudding', 'cheese-burger']

    myFoodList.pop()
    print(myFoodList)
    # output: ['cake strawberries', 'pizza', 'hamburger', 'pudding']

    myFoodList.sort()
    print(myFoodList)
    # output: ['cake strawberries', 'hamburger', 'pizza', 'pudding']

    myFoodList.reverse()
    print(myFoodList)
    # output: ['pudding', 'pizza', 'hamburger', 'cake strawberries']
