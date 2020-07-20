pet1 = {'name': 'Pup',
        'kind': 'dog',
        'owner': 'Abner',
        }

pet2 = {'name': 'Spot',
        'kind': 'dog',
        'owner': 'Tammy',
        }

pet3 = {'name': 'Mouse',
        'kind': 'cat',
        'owner': 'Dick',
        }

pets = [pet1, pet2, pet3]

for pet in pets:
    print(pet['name'])
    print(pet['kind'])
    print(pet['owner'])
    print("")
