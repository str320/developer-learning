cities = {
    "athens": {
        "country": "greece",
        "population": 3000000,
        "fact": "It is one of the world's oldest cities.",
        "cities": ["thessaloniki", "patras", "heraklion"],
    },
    "london": {
        "country": "united kingdom",
        "population": 9000000,
        "fact": "It is located on the River Thames.",
        "cities": ["manchester", "birmingham", "liverpool"],
    },
    "tokyo": {
        "country": "japan",
        "population": 37000000,
        "fact": "It is one of the largest metropolitan areas in the world.",
        "cities": ["osaka", "kyoto", "yokohama"],
    },
}

for city, info in cities.items():
    country = info["country"]
    population = info["population"]
    fact = info["fact"]

    print(f"\nCity: {city.title()}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")

    print(f"\n{country} other cities:")

    for city in info["cities"]:
        print(city.title())