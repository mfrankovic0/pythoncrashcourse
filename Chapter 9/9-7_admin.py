class User:
    """Creates a user and their attributes."""

    def __init__(self, first_name, last_name):
        """Store first and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Print attributes."""
        print(f"First Name = {self.first_name}")
        print(f"Last Name = {self.last_name}")

    def greet_user(self):
        """Greet the user using their name."""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Add 1 to login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0."""
        self.login_attempts = 0

    def display_login_attempts(self):
        """Self-explanatory."""
        print(f"{self.first_name} {self.last_name} has made {self.login_attempts} login attempts.")


class Admin(User):
    """Create a user with superuser privileges."""

    def __init__(self, first_name, last_name):
        """Add user attributes and superuser privileges."""
        super().__init__(first_name, last_name)
        self.privileges = ['add post', 'del post', 'edit post', 'ban user', 'reinstate user']

    def show_privileges(self):
        """Show privileges."""
        print(f"{self.first_name} {self.last_name} has the following privileges:\n {self.privileges}")

Jimbob = Admin('Jimbob', 'Orton')

Jimbob.show_privileges()