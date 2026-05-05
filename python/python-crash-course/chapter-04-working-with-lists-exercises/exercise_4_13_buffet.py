foods = ("rice", "beans", "salad", "soup", "bread")
# This would raise a TypeError because tuples are immutable:
# foods[1] = "steak"

print("Original menu:")
for food in foods:
    print(food)

foods = ("rice", "salad", "bread", "steak", "fish")

print("Revised menu:")
for food in foods:
    print(food)