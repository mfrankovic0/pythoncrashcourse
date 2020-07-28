responses = {}

polling_active = True

while polling_active:
    name = input("\nHello, what is your name? ")
    response = input("If you could go anywhere in the world, where would you go? ")

    responses[name] = response

    next = input("Is anyone next? ")
    if next == 'no':
        polling_active = False

print("\n---RESULTS---")
for name, response in responses.items():
    print(f"{name} would like to go to {response}!")
