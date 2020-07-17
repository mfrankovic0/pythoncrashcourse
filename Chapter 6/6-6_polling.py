favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = [
    'jimbob', 'jefferson', 'jen', 'edward', 'marie', 'sarah', 'phil'
]

for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll!")
    else:
        if name not in favorite_languages.keys():
            print(f"{name.title()}, you need to take the poll.")
