filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

newstring = ''
for line in lines:
    newstring += line.replace('Python', 'Golang') 

print(newstring.rstrip())