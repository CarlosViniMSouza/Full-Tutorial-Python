# 2D Lists -> A list of lists

class Lists2D:
    my2DList = [
        ['element', 'object'],
        ['people', 'code'],
    ]

    # Using some methods:

    # 1. append()
    my2DList.append(['Python', 'JS'])

    print(my2DList)
    # output: [['element', 'object'], ['people', 'code'], ['Python', 'JS']]

    # 2. remove()
    my2DList.remove(['people', 'code'])

    print(my2DList)
    # output: [['element', 'object'], ['Python', 'JS']]

    # 3. sort()
    my2DList.sort()

    print(my2DList)
    # output: [['Python', 'JS'], ['element', 'object']]
