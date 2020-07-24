topping = ("\nWhat topping would you like on your pizza?: ")
topping += ("\nEnter 'quit' to end the program. ")

message = ""
while message != 'quit':
    message = input(topping)
    print(message)