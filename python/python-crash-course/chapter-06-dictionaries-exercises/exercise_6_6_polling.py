# Exercise 6-6 — Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

people_to_poll = ["jen", "sarah", "erin", "phil", "ada"]

for person in people_to_poll:
    if person not in favorite_languages:
        print(f"{person.title()} we invite you to take the poll.\n")
    else:
        print(f"{person.title()} thank you for responding.\n")