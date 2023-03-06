# Tuples: collection of ordered and unchanging data

class Tuples:
    myTuple = ("Carlos", 22, True, 20768.24, ['One', 'Punch', 'Man'])

    print(myTuple.count(False)) # output: 0

    print(myTuple.index(20768.24)) # output: 3

    for elem in myTuple:
        print(elem)
        """
        # output:
        Carlos
        22
        True
        20768.24
        ['One', 'Punch', 'Man']
        """

    if 'Man' in myTuple[-1]:
        print('Man exists')
        # output: Man exists