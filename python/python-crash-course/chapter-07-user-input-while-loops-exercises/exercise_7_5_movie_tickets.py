# Exercise 7-5 — Movie Tickets

prompt = "\nEnter your age,"
prompt += "\nOr enter quit to stop: "

while True:
    age = input(prompt)

    if age.lower() == "quit":
        break

    age = int(age)

    if age < 3:
        print(f"Your ticket is free!")
    elif age <= 12:
        print(f"Your ticket costs $10!")
    else:
        print(f"Your ticket costs $15!")