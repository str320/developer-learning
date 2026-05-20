# Exercise 6-5 — Rivers

rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "danube": "germany",
}

for river, country in rivers.items():
    print(f"Country: {country.title()}")
    print(f"River: {river.title()}")
    print(f"The river {river.title()} is in {country.title()}\n")

for river in rivers.keys():
    print(f"The river is {river.title()}\n")

for country in rivers.values():
    print(f"The country of this river is {country.title()}\n")

