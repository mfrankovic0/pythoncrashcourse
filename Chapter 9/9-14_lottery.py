from random import choice

lottery = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f')
lucky = []

for i in range(4):
    number = choice(lottery)
    lucky.append(number)

print(f"Your lucky number are: ")

for luck in lucky:
    print(luck)