# Exercise 6-7 — People

person_1 = {
    "first_name": "john",
    "last_name": "lars",
    "age": 32,
    "city": "athens"
    }

person_2 = {
    "first_name": "ada",
    "last_name": "doe",
    "age": 24,
    "city": "munich",
    }

person_3 = {
    "first_name": "nicole",
    "last_name": "smith",
    "age": 28,
    "city": "berlin",
    }

persons = [person_1, person_2, person_3]

for person in persons:
    print(f"Name: {person["first_name"].title()} {person["last_name"].title()}")
    print(f"Age: {person["age"]}")
    print(f"City: {person["city"].title()}\n")