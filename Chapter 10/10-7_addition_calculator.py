while True:
    try:
        num1 = input("Type the first number.(Or type q to quit.)")
        if num1 == 'q':
            break
        
        x = int(num1)
        
        num2 = input("Type the secong number.(Or type q to quit)")
        if num2 == 'q':
            break
            
        y = int(num2)

    except ValueError:
        print("Sorry, we need a number.")
        
    else:
        print(x + y)