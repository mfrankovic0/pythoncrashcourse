p = 'poll.txt'
a = True

while a == True:
    name = input("Why do you like programming? (Or type Q to quit.)")
    if name == 'Q':
        a = False
        print("Guestbook is closed. Bye!")
    else:
        with open(p, 'a') as txt:
            txt.write(f"{name}\n")