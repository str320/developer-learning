# Exercise 7-2 — Restaurant Seating

prompt = "How many people are in your dinner group? "
answer = int(input(prompt))

if answer > 8:
    print(f"Sorry you will have to wait for a table of {answer}.")
else:
    print(f"Great your table for {answer} is ready.")