name = ("Please enter your name: ")
print(f"Hello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your name: "

name = input(prompt)
print(name)

age = input("How old are you: ")
age = int(age)

if age >= 18:
    print("you are allowed to vote")
else:
    print("You are to young")

