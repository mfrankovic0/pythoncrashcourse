cats = 'cats.txt'
dogs = 'dogs.txt'

try:
    print("Cats:")
    with open(cats) as c:
        for line in c:
            print(line.rstrip())

except FileNotFoundError:
    print(f"Sorry, {cats} not found.")

try:        
    print("\nDogs:")
    with open(dogs) as d:
        for line in d:
            print(line.rstrip())

except FileNotFoundError:
    print(f"Sorry, {dogs} not found.")