guests = ["Last Hope", "Ada Lovelace", "Stratos Hull", "Alan Turing", "Grace Hopper", "John Ripper",]

message = "Sorry i can invite only two guests for dinner."

ada = guests.pop(1)
print(f"\n{ada.title()}, {message}")

alan = guests.pop(2)
print(f"\n{alan.title()}, {message}")

grace = guests.pop(2)
print(f"\n{grace.title()} {message}")

john = guests.pop(-1)
print(f"\n{john} {message}")
print(f"\n{guests[0]} and {guests[1]} you are invited for dinner.")

del guests[0], guests[0]
print(guests)
