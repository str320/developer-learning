pizzas = ["margherita", "pepperoni", "vegetarian"]
friend_pizzas = pizzas[0:]
pizzas.append("mushroom")
friend_pizzas.append("special")

print(f"Original list: {pizzas}")
print(f"Modified list: {friend_pizzas}")

print(len(friend_pizzas) == len(pizzas))

print("\nThis is the original list:")
for pizza in pizzas:
    print(pizza)

print("\nThis is the modified list:")
for pizza in friend_pizzas:
    print(f"{pizza}")
