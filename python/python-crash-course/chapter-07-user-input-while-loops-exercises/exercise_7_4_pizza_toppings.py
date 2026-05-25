# Exercise 7-4 — Pizza Toppings

prompt = "\nEnter a pizza topping "
prompt += "\nor enter quit to stop: "

topping = ""

while topping.lower() != "quit":
    topping = input(prompt)

    if topping.lower() != "quit":
        print(f"{topping} is added to your pizza.")