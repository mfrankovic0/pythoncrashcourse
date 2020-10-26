guest = 'guestname.txt'

guestname = input("What is your name?")
with open(guest, 'w') as file_object:
    file_object.write(f"{guestname}")

with open(guest) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
