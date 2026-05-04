my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[0:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for foods in my_foods:
    print(foods)

print("\nMy friend's favorite foods are:")
for foods in friend_foods:
    print(foods)