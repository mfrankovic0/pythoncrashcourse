from random import randint

class Die:
    """Creates a die with a variable amount of sides."""
    def __init__(self, value):
        self.value = value

    def roll_die(self):
        print(randint(1, self.value))


print("6-sided die:")
die1 = Die(6)
for i in range(10):
    die1.roll_die()

print("10-sided die:")
die2 = Die(10)
for i in range(10):
    die2.roll_die()

print("20-sided die:")
die3 = Die(20)
for i in range(10):
    die3.roll_die()
