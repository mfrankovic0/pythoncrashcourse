#Copied from 4-1
pizzas = ['pepperoni', 'sausage', 'bacon', 'peppers', 'basil']

for pizza in pizzas:
    print(f"The best pizza has {pizza} on it!")

print("But any pizza is better than none!")

friends_pizzas = pizzas[:]
pizzas.append('extra cheese')
friends_pizzas.append('white')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('My friend\'s favorite pizzas are:')
for pizza in friends_pizzas:
    print(pizza)
