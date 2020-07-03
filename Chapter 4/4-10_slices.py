#Copied exercise 4-1
pizzas = ['pepperoni', 'sausage', 'bacon', 'peppers', 'basil']

for pizza in pizzas:
    print(f"The best pizza has {pizza} on it!")

print("But any pizza is better than none!")

print("The firse three items in the list are:")
for pizza in pizzas[:3]:
    print(pizza)

print("Three items from the middle of the list are:")
for pizza in pizzas[1:4]:
    print(pizza)

print("The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)
