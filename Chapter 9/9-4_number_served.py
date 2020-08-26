class Restaurant:
    """A restaurant model."""

    def __init__(self, name, kind):
        """Initialize name and type."""
        self.restaurant_name = name
        self.cuisine_kind = kind
        self.number = 0

    def describe_restaurant(self):
        """Describes restaurant name and type."""
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_kind}.")
    
    def open_restaurant(self):
        """Indicates if restaurant is open."""
        print(f"{self.restaurant_name} is open.")

    def number_served(self):
        """Display number served."""
        print(f'Serving {self.number} currently.')

    def set_number_served(self, number):
        """Sets number served."""
        self.number = number

    def increment_number_served(self, number):
        """Sets number incrementlyby adding only."""
        self.number += number

restaurant = Restaurant('Taco Bell', 'Mexican')

#Display number served.
restaurant.number_served()

#Change number served directly to 5 and display it.
restaurant.number = 5
restaurant.number_served()

#Use method to change number served and display it.
restaurant.set_number_served(10)
restaurant.number_served()

#Use incremental method and display it.
restaurant.increment_number_served(20)
restaurant.number_served()
