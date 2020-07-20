person = {'first_name': 'Jethro',
          'last_name': 'Johnson-Teller',
          'age': '32',
          'city': 'Chattanooga'
          }

person2 = {'first_name': 'Marie',
           'last_name': 'Lancaster',
           'age': '19',
           'city': 'Fayetteville'
           }

person3 = {'first_name': 'Morrison',
           'last_name': 'Alder',
           'age': '24',
           'city': 'Orlando'
           }

persons = [person, person2, person3]

for people in persons:
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])
    print("")
