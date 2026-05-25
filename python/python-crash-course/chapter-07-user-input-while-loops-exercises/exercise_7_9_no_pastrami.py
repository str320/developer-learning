# Exercise 7-9 — No Pastrami

sandwich_orders = ["tuna", "pastrami", "veggie", "pastrami", "club", "pastrami"]
finished_sandwiches = []

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("The deli has run out of pastrami!")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    
    print(f"I made your {current_sandwich.title()} sandwich.")

for sandwich in finished_sandwiches:
    print(sandwich.title())