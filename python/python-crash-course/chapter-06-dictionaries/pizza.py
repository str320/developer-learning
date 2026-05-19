# A List in a Dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f"You ordered a {pizza["crust"]} -crust pizza "
      "With the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping}")