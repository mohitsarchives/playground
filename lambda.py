people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

try:
    people.sort(key = lambda person: person["house"])
except TypeError:
    print("This cannot be sorted.")
else:
    print(people)