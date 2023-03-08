"""
Set -> collection of data unordered and unindexed.
Without data duplicated.
"""


class SetExample:
    mySet = {'Carlos', 22, True, 20082.34}
    otherSet = {'PY', 'JS', 'PHP'}
    lastSet = {'Carlos', 24, False}

    # Any methods for sets:

    # 1. add() -> insert a new element
    mySet.add('Text')

    print(mySet)

    # 2. remove() -> delete a specific element
    mySet.remove(True)

    print(mySet)

    # 3. update() -> insert a set in other set
    mySet.update(otherSet)

    print(mySet)

    # 4. intersection() -> check if a element in other set
    result = mySet.intersection(lastSet)

    print(result)

    # 5. difference() -> return the element not present in the set
    # opposite the 'intersection() method'
    result = mySet.difference(lastSet)

    print(result)
