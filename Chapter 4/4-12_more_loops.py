#Copied foods.py from page 63
my_foods = ['pizza', 'falafel', 'carrot cake']

print('My favorite foods are:')
for food in my_foods:
    print(food)

friends_foods = my_foods[:]
friends_foods.append('ice cream')

print('My friend\'s favorite foods are:')
for food in friends_foods:
    print(food)