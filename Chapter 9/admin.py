from user import User

class Admin(User):
    """Create a user with superuser privileges."""

    def __init__(self, first_name, last_name):
        """Add user attributes and superuser privileges."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

class Privileges:
    """Stores privileges and shows them."""

    def __init__(self):
        """Stores privileges."""
        self.privileges = ['add post', 'del post', 'edit post', 'ban user', 'reinstate user']

    def show_privileges(self):
        """Show privileges."""
        print(f"Privileges:\n {self.privileges}")