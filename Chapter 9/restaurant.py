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
