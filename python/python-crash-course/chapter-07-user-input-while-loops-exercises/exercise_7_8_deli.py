# Exercise 7-8 — Deli

sandwich_orders = ["tuna", "pastrami", "veggie"]
finished_sandwiches = []

while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f"\nI made your {current_sandwich.title()} sandwich.")
        finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"\n{sandwich.title()} sandwich")