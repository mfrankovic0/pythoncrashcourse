cities = {
    'Zagreb': {
        'country': 'Croatia',
        'pop': '800 000',
        'fact': 'Zagreb has more museums per capita than anywhere else in the world.'
    },
    'Tampa': {
        'country': 'USA',
        'pop': '400 000',
        'fact': 'John Cena was born in Tampa.'
    },
    'Macau': {
        'country': 'China',
        'pop': '700 000',
        'fact': 'Macau was formerly a colony of the Portuguese Empire.'
    }
}

for city, city_info in cities.items():
    print(f"\nCity: {city}")
    country = city_info['country']
    population = city_info['pop']
    fact = city_info['fact']

    print(f"Country: {country}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")
