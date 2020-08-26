class User:
    """Creates a user and their attributes."""

    def __init__(self, first_name, last_name):
        """Store first and last name."""
        self.first_name = first_name
        self.last_name = last_name 

    def describe_user(self):
        """Print attributes."""
        print(f"First Name = {self.first_name}")
        print(f"Last Name = {self.last_name}")
    
    def greet_user(self):
        """Greet the user using their name."""
        print(f"Hello, {self.first_name} {self.last_name}!")

Jimmy = User('Jimbob', 'Thorton')
Marie = User('Marie-Ann', 'Fletcherson')
Tabby = User('Tabitha', 'Lambert')

Jimmy.describe_user()
Jimmy.greet_user()

Marie.describe_user()
Marie.greet_user()

Tabby.describe_user()
Tabby.greet_user()