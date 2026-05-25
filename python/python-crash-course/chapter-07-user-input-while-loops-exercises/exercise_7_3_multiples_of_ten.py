# Exercise 7-3 — Multiples of Ten

prompt = "Please Enter a number: "
number = int(input(prompt))

if number % 10 == 0:
    print(f"This number {number} is multiple of 10.")
else:
    print(f"Sorry the number {number} is not multiple of 10")