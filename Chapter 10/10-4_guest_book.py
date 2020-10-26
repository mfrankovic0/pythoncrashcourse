g = 'guestbook.txt'
a = True

while a == True:
    name = input("Welcome to the party. What is your name?(Or type Q to quit.)")
    if name == 'Q':
        a = False
        print("Guestbook is closed. Bye!")
    else:
        with open(g, 'a') as txt:
            txt.write(f"{name}\n")
