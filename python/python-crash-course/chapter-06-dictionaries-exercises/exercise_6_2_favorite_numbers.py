# Exercise 6-2 — Favorite Numbers

favorite_numbers = {
    "ada": 10,
    "john": 3,
    "hope": 24,
    "mike": 14,
    "maria": 34,
    }

for name, number in favorite_numbers.items():
    print(f"\nname: {name.title()}")
    print(f"favorite number: {number}")