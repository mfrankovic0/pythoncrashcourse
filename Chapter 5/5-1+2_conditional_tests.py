car = 'audi'

print("Is car == 'subaru'? I predict False.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict True.")
print(car == 'audi')

print("\nIs the car name capitalized?")
print(car == 'Audi')

print("\nIs the car name capitalized now?")
print(car.title() == 'Audi')

print("\nLet's make it permanently capitalized.")
car = car.title()
print(car == 'Audi')

print("\nMake sure first!")
print(car == 'audi')

print("\nNow let's use the lower() method.")
print(car.lower() == 'audi')

print("\nDouble check now.")
print(car != 'audi')

print("\nAre you sure it is not a Chevy?")
print(car == 'chevy')

print("\nHow many Audis are there in the street?")
Audis = '3'
print(f"There are {Audis} {car}s in the street.")

print("\nAre you sure?")
print(Audis == '3')

print("\nAre there more?")
print(Audis > '3')

print("\nAre there less than 3 or less?")
print(Audis <= '3')

print("\nNot less than 3?")
print(Audis < '3')

print("\nSo not more or less than 3?")
print(Audis < '3' and Audis > '3')

print("\nIs it either less than or equal to 3?")
print( Audis < '3' or Audis == '3')

cars = ['chevy', 'audi', 'lamborghini', 'yugo']

print("\nIs there a lamborghini in the street too?")
print('lamborghini' in cars)

print("\nIs there a ford in the street too?")
if 'ford' not in cars:
    print("No, there is not.")