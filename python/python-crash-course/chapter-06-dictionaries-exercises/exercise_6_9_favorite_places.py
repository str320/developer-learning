# Exercise 6-9 — Favorite Places

favorite_places = {
    "ada": ["london", "paris"],
    "grace": ["new york", "boston"],
    "alan": ["manchester", "cambridge"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} favorite places are:")

    for place in places:
        print(f"{place.title()}")