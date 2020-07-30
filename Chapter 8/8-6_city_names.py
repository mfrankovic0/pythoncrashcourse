def city_country(city, country):
    """Return a city and country."""
    city = f"{city}, {country}"
    return city.title()


city_name = city_country('Boulder', 'USA')
print(city_name)

city_name = city_country('Roppongi', 'Japan')
print(city_name)

city_name = city_country('Johannesburg', 'South Afrika')
print(city_name)