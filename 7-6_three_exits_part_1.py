#Using exercise 7-5 to clean up the code with an 'active' variable

message = ("\nWhat is your age?")
message += ("\nOr enter 'quit' to end the program: ")

active = True
while active:
    age = input(message)

    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age >= 3 and age < 12:
            print("Your ticket will be $10.")
        else:
            print("Your ticket will be $15.")