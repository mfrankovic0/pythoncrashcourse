def car_data(make, model, **other):
    """A car database."""
    other['make'] = make
    other['model'] = model
    return other

car_profile = car_data('Lamborghini', 'Diablo', year='1995', engine='5.7L V12')

print(car_profile)