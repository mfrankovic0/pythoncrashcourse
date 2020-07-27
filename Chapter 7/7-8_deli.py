sandwich_orders = [
    'italian', 'ham and cheese',
    'cuban', 'chicken parm', 'meatball',
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I have made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)

print("\nTHe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())