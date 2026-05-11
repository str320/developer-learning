# Exercise 2-1 — Simple Message

message = "I am learning Python."
print(message)

# Exercise 2-2 — Simple Messages

message = "I am learning python."
print(message)

message = "I am also learning javascript"
print(message)

# Exercise 2-3 — Personal Message

name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

# Exercise 2-4 — Name Cases

name = "Eric"
print(name.title())
print(name.upper())
print(name.lower())

# Exercise 2-5 — Famous Quote

name = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."

print(f"{name}, {quote}")

# Exercise 2-6 — Famous Quote 2

famous_person = "Albert Einstein, "
quote = "A person who never made a mistake never tried anything new."
message = famous_person + quote
print(message)

# Exercise 2-7 — Stripping Names

name = "\tEric\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Exercise 2-8 — File Extensions

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

# Exercise 2-9 — Number Eight

print(2 * 4)
print(4 + 4)
print(10 - 2)
print((8 // 2) + 4)

# Exercise 2-9 — Number Eight

favorite_number = 8
message = f"My favorite number is {favorite_number}."
print(message)

# Exercise 2-11 — Adding Comments

name = "\tEric\n"
print(name)

# This method removes the white space left side of the string
print(name.lstrip())
print(name.rstrip())
print(name.strip())

famous_person = "Albert Einstein, "
quote = "A person who never made a mistake never tried anything new."
# Using addition with strings we concatenate then in one string
message = famous_person + quote
print(message)