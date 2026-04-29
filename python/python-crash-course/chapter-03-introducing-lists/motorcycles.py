#Modifying, Adding, and Removing Elements

#Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print("This is the list.\n", motorcycles)

motorcycles[0] = "Ducati"
print(f"\nModified the 1st item with new name ({motorcycles[0].title()}).\n", motorcycles)

#Appending Elements to the End of a List
motorcycles.append("Ducati")
print(f"\nWe added a new item at the end of the list with the name ({motorcycles[-1]}).\n", motorcycles)

#Inserting Elements into a List
motorcycles.insert(1, "Piaggio")
print(f"\nWe inserted an item at second position with index 1 and the name ({motorcycles[1].title()}).\n", motorcycles)

#Removing an Item Using the del Statement
del motorcycles[0]
print(f"\nWe deleted the first item with name Ducati.\n", motorcycles)

#Removing an Item Using the pop() Method and keep it's value
popped_motorcycle = motorcycles.pop()
print(f"\nTThe last motorcycle I owned was a {popped_motorcycle.title()} and was popped from the list.\n", motorcycles)

#Remember that each time you use pop(), the item you work with is no longer stored in the list.
first_owned = motorcycles.pop(0)
print(f"\nThe first motorcycle I owned was a {first_owned.title()} also popped from the list.\n", motorcycles)

#Removing an Item by Value
motorcycles.remove("yamaha")
print(f"\nThe item with name Yamaha was removed from the list.\n", motorcycles)

too_expensive = "suzuki"
motorcycles.remove(too_expensive)
print(f"\n{too_expensive.title()} is too expensive and it was removed from the list.\n")
print(motorcycles)
print(f"\nThe list is empty now!!!\n", motorcycles)