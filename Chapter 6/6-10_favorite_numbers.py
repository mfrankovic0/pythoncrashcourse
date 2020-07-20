people = {'Jenny': ['3'],
          'Jimbob': ['8', '3'],
          'Marie': ['1', '55', '10'],
          'Talbot': ['14'],
          'Darleen': ['37', '35']
          }

for name, numbers in people.items():
    print(f"{name}:")
    for number in numbers:
        print(f"{number}")
    print("")
