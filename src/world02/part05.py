"""
dictionary -> collection of changeable, unordered data of unique key:value pairs
Fast because they use hashing, allow access a value quickly 
"""


class DictionariesMethods:
    myDict = {
        'Acre': 'Rio Branco',
        'Amapa': '...',
        'Amazonas': 'Manaus',
        'Rorraima': 'Boa Vista',
        'Para': 'Belem',
        'Tocantins': 'Palmas',
        'Rondonia': 'Porto Velho'
    }

    myDict.update({'Maranhao': 'Sao Luis'})
    print(myDict)
    """
    # output: 
    {
        'Acre': 'Rio Branco', 
        'Amapa': '...', 
        'Amazonas': 'Manaus', 
        'Rorraima': 'Boa Vista', 
        'Para': 'Belem', 
        'Tocantins': 'Palmas', 
        'Rondonia': 'Porto Velho', 
        'Maranhao': 'Sao Luis'
    }
    """
    
    myDict.pop('Para')
    print(myDict)
    """
    # output: 
    {
        'Acre': 'Rio Branco', 
        'Amapa': '...', 
        'Amazonas': 'Manaus', 
        'Rorraima': 'Boa Vista', 
        'Para': 'Belem', 
        'Tocantins': 'Palmas', 
        'Rondonia': 'Porto Velho', 
        'Maranhao': 'Sao Luis'
    }
    """
    
    print(myDict['Amazonas'])
    # output: Manaus
    
    print(myDict.get('Acre'))
    # output: Rio Branco
