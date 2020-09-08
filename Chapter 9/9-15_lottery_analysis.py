from random import choice

lottery = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
lucky = []
my_ticket = []
draws = 0
win = 0

def draw():
    """Draws 4 numbers and adds 1 to number of draws"""
    global lucky
    global draws
    for i in range(4):
        number = choice(lottery)
        lucky.append(number)
    draws += 1

def compare():
    """Sorts the two lists and compares them, changing win to 1 if return is true."""
    global my_ticket 
    global lucky
    global win
    lucky.sort()
    my_ticket.sort()
    if lucky == my_ticket:
        win = 1


for i in range(4):
     number = choice(lottery)
     my_ticket.append(number)


while True:
    draw()
    compare()
    if win == 1:
        print(f"We have a winner! It took {draws} draws for you to win.")
        print(lucky)
        print(my_ticket)
        break
    else:
        lucky = []
        
    


