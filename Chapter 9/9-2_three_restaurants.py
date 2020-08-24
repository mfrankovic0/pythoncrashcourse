class Restaurant:
    """A restaurant model."""

    def __init__(self, name, kind):
        """Initialize name and type."""
        self.restaurant_name = name
        self.cuisine_kind = kind

    def describe_restaurant(self):
        """Describes restaurant name and type."""
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_kind}.")
    
    def open_restaurant(self):
        """Indicates if restaurant is open."""
        print(f"{self.restaurant_name} is open.")

restaurant = Restaurant('Taco Bell', 'Mexican')
restaurant2 = Restaurant('McDonalds', 'Americana')
restaurant3 = Restaurant('KFC', 'Country-style')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()