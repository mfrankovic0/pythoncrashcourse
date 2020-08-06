def sandwich_maker(*stuff):
    """Lists all sandwich constituents."""
    print("\nThe next sandwich order: ")
    for things in stuff:
        print(things)

sandwich_maker('ham', 'american cheese', 'mayo')

sandwich_maker('bacon', 'lettuce', 'tomato', 'mayo')

sandwich_maker('prosciutto', 'soppressata', 'mozzerella', 'vinaigrette')