#Organizing a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"This is the list: ", cars)

#Sorting a List Permanently with the sort() Method
cars.sort()
print(f"\nThis is the list sorted in alphabetical order: ", cars)

cars.sort(reverse=True)
print(f"\nThis is the list sorted in reverse: ", cars)

#Sorting a List Temporarily with the sorted() Function
print(f"\nHere is the list: ", cars)

print(f"\nHere is the list sorted temporarily: ", sorted(cars))

print(f"\nHere is the list back in normal order: ", cars)

#Printing a List in Reverse Order
print(f"\nThis is the list again: ", cars)

cars.reverse()
print(f"\nThis is the list in reverse order: ", cars)

#Finding the Length of a List
print(f"\nFind the length of the list using the len() function:", len(cars))