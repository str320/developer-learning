my_foods = ['pizza', 'falafel', 'carrot cake']

#To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:])
friend_foods = my_foods[ : ]
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("Cannoli")
friend_foods.append("Ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)