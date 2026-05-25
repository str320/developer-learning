# Exercise 7-6 — Three Exits

prompt = "\nEnter your age,"
prompt += "\nOr enter quit to stop: "

# Version 1 — Conditional test in the while statement

is_age = ""

while is_age.lower() != "quit":
    is_age = input(prompt)

    if is_age != "quit":
        age = int(is_age)

        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket price is 10$!") 
        else:
            print("Your ticket price is 15$!")

# Version 2 — Active variable

is_age = True

while is_age:

    age = input(prompt)

    if age.lower() == "quit":
        is_age = False
    else:
        age = int(age)
    
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket price is 10$!") 
        else:
            print("Your ticket price is 15$!")

# Version 3 — break statement

is_age = " "

while is_age:
    is_age = input(prompt)

    if is_age.lower() == "quit":
        break

    age = int(is_age)

    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket price is 10$!") 
    else:
        print("Your ticket price is 15$!")