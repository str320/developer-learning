places = ["japan", "canada", "iceland", "new zealand", "peru"]

print(f"\nThis is the original list:", places)

print(f"\nThis is the list sorted:", sorted(places))

print(f"\nThis is the original list again:", places)

print(f"\nThis is the list in reverse:", sorted(places, reverse=True))

print(f"\nThis is the original list again:", places)

places.reverse()
print(f"\nThis is the list modified in reverse:", places)

places.reverse()
print(f"\nThis is the list reversed back to original:", places)

places.sort()
print(f"\nThis is the list permanently sorted:", places)

places.sort(reverse=True)
print(f"\nThis is the list again in reverse alphabetical order:", places)