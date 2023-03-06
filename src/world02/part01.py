class Lists:
    myFoodList = ['pizza', 'hamburger', 'hot-dog', 'pudding']

    print(myFoodList[1])
    # output: 'hamburger'

    # Methods for handle lists:

    # 1. append() -> add a element to end of list
    myFoodList.append('cheese-burger')

    print(myFoodList)
    # output: ['pizza', 'hamburger', 'hot-dog', 'pudding', 'cheese-burger']

    # 2. remove() -> delete a specific element from the list
    myFoodList.remove('hot-dog')

    print(myFoodList)
    # output: ['pizza', 'hamburger', 'pudding', 'cheese-burger']
    
    # 3. insert() -> add a element in the specific position
    myFoodList.insert(0, 'cake strawberries')

    print(myFoodList)
    # output: ['cake strawberries', 'pizza', 'hamburger', 'pudding', 'cheese-burger']

    # 4. pop() -> delete the last element from list
    myFoodList.pop()
    
    print(myFoodList)
    # output: ['cake strawberries', 'pizza', 'hamburger', 'pudding']

    # 5. sort() -> literally, sort the list alphabetically
    myFoodList.sort()
    
    print(myFoodList)
    # output: ['cake strawberries', 'hamburger', 'pizza', 'pudding']

    # 6. reverse() -> literally, invert the list alphabetically ()
    # NOTE: opposite of 'sort()' method
    myFoodList.reverse()

    print(myFoodList)
    # output: ['pudding', 'pizza', 'hamburger', 'cake strawberries']
