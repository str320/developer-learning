# Exercise 7-10 — Dream Vacation

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place
    
    repeat = input("If you want another person to take the poll answer yes/no? ")
    
    if repeat.lower() == "no":
        polling_active = False

print("\nPoll Results:")

for name, place in responses.items():
    print(f"{name.title()} : {place.title()}")