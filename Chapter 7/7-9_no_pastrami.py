sandwich_orders = [
    'italian', 'pastrami', 'ham and cheese',
    'cuban', 'pastrami', 'chicken parm', 'pastrami',
    'meatball',
]

print("We have run out of pastrami, sorry!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I have made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)

print("\nTHe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
