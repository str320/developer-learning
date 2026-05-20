# Exercise 6-10 — Favorite Numbers

favorite_numbers = {
    "ada": [7, 11],
    "john": [42, 3],
    "hope": [9, 14],
    "mike": [3, 8],
    "maria": [11, 21],
    }

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()} favorite numbers are:")
    
    for number in numbers:
        print(number)
