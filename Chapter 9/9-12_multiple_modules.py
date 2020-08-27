#from user import User as U
from admin import Admin as A, Privileges as P


Jimmy = A('Jimbob', 'Orton')

Jimmy.privileges.show_privileges()