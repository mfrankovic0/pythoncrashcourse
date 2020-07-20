favorite_places = {
    'Johnny': ['Brazil', 'Jamaica'],
    'Tammy': ['Australia', 'Israel'],
    'Olaf': ['Algeria', 'Scotland', 'Mexico']
}

for name, places in favorite_places.items():
    print(f"{name}:")
    for places in places:
        print(f"{places}")
    print("")
