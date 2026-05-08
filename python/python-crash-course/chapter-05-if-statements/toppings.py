requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!\n")

# Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("Finished making your pizza!")

# Using if Statements with Lists

if requested_topping in requested_toppings:
    print(f"\nAdding {requested_topping}")

print("Finished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("\nSorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("Finished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?\n")

# Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese',  'pineapple']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("Finish making your pizza!")