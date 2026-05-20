# Exercise 6-8 — Pets

pet_1 = {
    "animal": "dog",
    "owner": "ada",
}

pet_2 = {
    "animal": "cat",
    "owner": "grace",
}

pet_3 = {
    "animal": "parrot",
    "owner": "alan",
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Animal: {pet["animal"].title()}")
    print(f"Owner: {pet["owner"].title()}\n")