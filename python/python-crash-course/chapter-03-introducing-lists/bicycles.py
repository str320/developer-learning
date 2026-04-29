#A list is a collection of items in particular. order
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.
print(bicycles[0])

#You can also use the string methods
print(bicycles[0].title())

#Index Positions Start at 0, Not 1
print(bicycles[1].upper())
print(bicycles[2].lower())
print(bicycles[-1].title())

#Using Individual Values from a List
message = f"My first bicycle was a {bicycles[1].title()}."
print(message)