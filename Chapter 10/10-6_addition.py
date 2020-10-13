try:
    num1 = input("Type the first number.")
    x = int(num1)
    
    num2 = input("Type the secong number.")
    y = int(num2)

except ValueError:
    print("Sorry, we need a number.")
    
else:
    print(x + y)