message = ("\nWhat is your age?")
message += ("\nOr enter 'quit' to end the program: ")

age = ""
while age != "quit":
    age = input(message)
    if age == "quit":
        print(age)
    else:
        age2 = int(age)
        if age2 < 3:
            print("Your ticket is free!")
        elif age2 >= 3 and age2 < 12:
            print("Your ticket will be $10.")
        else:
            print("Your ticket will be $15.")