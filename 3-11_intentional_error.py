#Copied from exercise 3-10, we create an interntional index error here at line 15.
njtowns = ['North Bergen', 'New Rochelle', 'Secaucus', 'Paramus', 'Edgewater', 'Franklin Lakes', 'New Brunswick',]

print(njtowns)

print(njtowns[3])

print(njtowns[2].title())

print(njtowns[-1])

msg = f"I was born in {njtowns[2]}."
print(msg)

njtowns[9] = 'Ramsey'
print(njtowns)

njtowns.append('New Brunswick')
print(njtowns)

njtowns.insert(3, 'Teterboro')
print(njtowns)

del njtowns[7]
print(njtowns)

popped_town = njtowns.pop(7)
print(f"I don't go to {popped_town} often.")

too_small = 'Teterboro'
njtowns.remove(too_small)
print(f"{too_small} is too small of a town.")

njtowns.sort()
print(njtowns)

njtowns.sort(reverse=True)
print(njtowns)

print(sorted(njtowns))
print(njtowns)

njtowns.sort()
print(njtowns)

njtowns.reverse()
print(njtowns)

print(len(njtowns))
