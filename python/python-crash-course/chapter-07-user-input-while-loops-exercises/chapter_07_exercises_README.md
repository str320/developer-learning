# Python Crash Course — Chapter 7 Exercises

## Chapter 7 — User Input and While Loops

This folder contains practice exercises for **Python Crash Course Chapter 7: User Input and While Loops**.

The goal of this chapter is to learn how to:

- use `input()` to collect user input
- remember that `input()` returns a string
- convert input with `int()` when working with numbers
- use the modulo operator `%`
- write `while` loops
- stop a loop with a conditional test
- stop a loop with an active flag
- stop a loop with `break`
- skip one loop iteration with `continue`
- avoid accidental infinite loops
- move items from one list to another
- remove all matching values from a list
- fill a dictionary with user input
- format user-facing output clearly
- continue reading official Python documentation

Recommended folder:

```text
python/python-crash-course/chapter-07-user-input-and-while-loops-exercises
```

Recommended files:

```text
README.md
exercise_7_1_rental_car.py
exercise_7_2_restaurant_seating.py
exercise_7_3_multiples_of_ten.py
exercise_7_4_pizza_toppings.py
exercise_7_5_movie_tickets.py
exercise_7_6_three_exits.py
exercise_7_7_infinity.py
exercise_7_8_deli.py
exercise_7_9_no_pastrami.py
exercise_7_10_dream_vacation.py
```
---

# Example — Basic Input

## Task

Ask the user for their name and print a greeting.

## Concepts

- `input()`
- variables
- f-strings
- user-facing prompts

## Starter code

```python
name = input("Please enter your name: ")
```

<details>
<summary>Show starter code</summary>

```python
name = input("Please enter your name: ")
print(f"Hello, {name.title()}!")
```

</details>

## Goal

Understand that `input()` pauses the program, waits for the user to type something, and returns that input as a string.

---

# Example — Numeric Input

## Task

Ask the user for their age and check whether they are old enough to vote.

## Concepts

- `input()`
- `int()`
- comparison
- `if-else`

## Starter code

```python
age = input("How old are you? ")
```

<details>
<summary>Show starter code</summary>

```python
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are too young to vote.")
```

</details>

## Goal

Understand that user input must be converted to a number before doing numeric comparisons.

---

# Example — while Loop

## Task

Use a `while` loop to repeat a message until the user types `"quit"`.

## Concepts

- `while`
- loop condition
- sentinel value
- user input

## Starter code

```python
prompt = "Enter a message, or 'quit' to stop: "
message = ""
```

<details>
<summary>Show starter code</summary>

```python
prompt = "Enter a message, or 'quit' to stop: "
message = ""

while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)
```

</details>

## Goal

Understand how a `while` loop repeats while its condition is true.

---

# Exercise 7-1 — Rental Car

## Task

Write a program that asks the user what kind of rental car they would like.

Print a message about that car, such as:

```text
Let me see if I can find you a Subaru.
```

## Concepts

- `input()`
- variables
- f-strings
- user-facing output

## Starter code

```python
car = input("What kind of rental car would you like? ")
```

<details>
<summary>Show starter code</summary>

```python
car = input("What kind of rental car would you like? ")

print(f"Let me see if I can find you a {car.title()}.")
```

</details>

## Goal

Practice collecting simple text input and using that input in a message.

---

# Exercise 7-2 — Restaurant Seating

## Task

Write a program that asks the user how many people are in their dinner group.

Rules:

1. If the answer is more than `8`, print a message saying they will have to wait for a table.
2. Otherwise, report that their table is ready.

## Concepts

- `input()`
- `int()`
- numerical comparison
- `if-else`

## Starter code

```python
group_size = input("How many people are in your dinner group? ")
```

<details>
<summary>Show starter code</summary>

```python
group_size = input("How many people are in your dinner group? ")
group_size = int(group_size)

if group_size > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
```

</details>

## Goal

Practice converting user input from a string to an integer before comparing it.

---

# Exercise 7-3 — Multiples of Ten

## Task

Ask the user for a number.

Report whether the number is a multiple of `10`.

## Concepts

- `input()`
- `int()`
- modulo `%`
- `if-else`
- divisibility

## Starter code

```python
number = input("Enter a number: ")
```

<details>
<summary>Show starter code</summary>

```python
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
```

</details>

## Goal

Practice using `%` to check whether one number divides evenly into another.

---

# Exercise 7-4 — Pizza Toppings

## Task

Write a loop that prompts the user to enter a series of pizza toppings.

Rules:

1. Keep asking for toppings until the user enters `"quit"`.
2. As each topping is entered, print a message saying you will add that topping to their pizza.

## Concepts

- `while`
- `input()`
- sentinel value
- loop condition
- f-strings

## Starter code

```python
prompt = "Enter a pizza topping, or 'quit' to stop: "
```

<details>
<summary>Show starter code</summary>

```python
prompt = "Enter a pizza topping, or 'quit' to stop: "
topping = ""

while topping != "quit":
    topping = input(prompt)

    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")
```

</details>

## Goal

Practice using a loop that stops when the user enters a specific value.

---

# Exercise 7-5 — Movie Tickets

## Task

A movie theater charges different ticket prices depending on a person's age.

Rules:

- Under age `3`: ticket is free
- Age `3` through `12`: ticket is `$10`
- Over age `12`: ticket is `$15`

Write a loop that asks users their age and tells them the cost of their movie ticket.

## Concepts

- `while`
- `input()`
- `int()`
- `if-elif-else`
- ordered conditions
- sentinel value

## Starter code

```python
prompt = "Enter your age, or 'quit' to stop: "
```

<details>
<summary>Show starter code</summary>

```python
prompt = "Enter your age, or 'quit' to stop: "

while True:
    age = input(prompt)

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
```

</details>

## Goal

Practice combining user input, numeric conversion, loops, and ordered conditions.

---

# Exercise 7-6 — Three Exits

## Task

Write different versions of either Exercise 7-4 or Exercise 7-5.

Use each loop-control pattern at least once:

1. Use a conditional test in the `while` statement to stop the loop.
2. Use an active variable to control how long the loop runs.
3. Use a `break` statement to exit the loop when the user enters `"quit"`.

## Concepts

- `while` condition
- active flag
- `break`
- loop control
- comparing loop styles

## Starter code

```python
prompt = "Enter a pizza topping, or 'quit' to stop: "
```

<details>
<summary>Show starter code</summary>

```python
# Version 1 — Conditional test in the while statement

prompt = "Enter a pizza topping, or 'quit' to stop: "
topping = ""

while topping != "quit":
    topping = input(prompt)

    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")


# Version 2 — Active variable

active = True

while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")


# Version 3 — break statement

while True:
    topping = input(prompt)

    if topping == "quit":
        break

    print(f"I'll add {topping} to your pizza.")
```

</details>

## Goal

Compare three common ways to stop a `while` loop and learn when each style is readable.

---

# Exercise 7-7 — Infinity

## Task

Write a loop that never ends and run it.

To end the loop, press:

```text
CTRL-C
```

or close the terminal/window displaying the output.

## Concepts

- infinite loop
- `while True`
- debugging
- stopping a running program

## Starter code

```python
while True:
    ...
```

<details>
<summary>Show starter code</summary>

```python
while True:
    print("This loop will run forever.")
```

</details>

## Goal

Understand what an infinite loop looks like and how to stop one safely.

## Warning

Only run this exercise when you are ready to stop it with `CTRL-C`.

---

# Exercise 7-8 — Deli

## Task

Make a list called `sandwich_orders` and fill it with the names of various sandwiches.

Then make an empty list called `finished_sandwiches`.

Steps:

1. Loop through the list of sandwich orders.
2. Print a message for each order, such as:
   ```text
   I made your tuna sandwich.
   ```
3. As each sandwich is made, move it to the list of finished sandwiches.
4. After all sandwiches have been made, print a message listing each sandwich that was made.

## Concepts

- lists
- `while`
- `.pop()`
- `.append()`
- moving items between lists
- truth value testing

## Starter code

```python
sandwich_orders = ["tuna", "pastrami", "veggie"]
finished_sandwiches = []
```

<details>
<summary>Show starter code</summary>

```python
sandwich_orders = ["tuna", "pastrami", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")

for sandwich in finished_sandwiches:
    print(sandwich.title())
```

</details>

## Goal

Practice using a `while` loop to process all items in a list.

---

# Exercise 7-9 — No Pastrami

## Task

Use the list `sandwich_orders` from Exercise 7-8.

Rules:

1. Make sure `"pastrami"` appears in the list at least three times.
2. Print a message saying the deli has run out of pastrami.
3. Use a `while` loop to remove all occurrences of `"pastrami"` from `sandwich_orders`.
4. Make sure no pastrami sandwiches end up in `finished_sandwiches`.

## Concepts

- lists
- `while item in list`
- `.remove()`
- `.pop()`
- `.append()`
- filtering values before processing

## Starter code

```python
sandwich_orders = ["tuna", "pastrami", "veggie", "pastrami", "club", "pastrami"]
finished_sandwiches = []
```

<details>
<summary>Show starter code</summary>

```python
sandwich_orders = ["tuna", "pastrami", "veggie", "pastrami", "club", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")

for sandwich in finished_sandwiches:
    print(sandwich.title())
```

</details>

## Goal

Practice removing all matching values before processing the remaining items.

---

# Exercise 7-10 — Dream Vacation

## Task

Write a program that polls users about their dream vacation.

Ask a prompt similar to:

```text
If you could visit one place in the world, where would you go?
```

Include a block of code that prints the results of the poll.

## Concepts

- dictionaries
- `while`
- active flag
- `input()`
- `.items()`
- polling
- storing user responses

## Starter code

```python
responses = {}
polling_active = True
```

<details>
<summary>Show starter code</summary>

```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat.lower() == "no":
        polling_active = False

print("\nPoll results:")

for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
```

</details>

## Goal

Practice filling a dictionary with user input and looping through the results.

---

# Official Docs Practice

Chapter 7 introduces user input and `while` loops, so official documentation practice should focus on input/output and compound statements.

Read selectively. Do not try to understand the entire documentation page at once.

## Docs sections to inspect

```text
Built-in Functions — input()
Built-in Functions — int()
Compound Statements — while
Simple Statements — break
Simple Statements — continue
```

Use this checklist:

```text
1. What problem does this feature solve?
2. What syntax does it use?
3. What does it return?
4. Does it mutate or change an object?
5. Can it raise an error?
6. Can I run one tiny example?
7. What mistake should I avoid?
```

## Small experiments

Add these to `notes.md` or `docs_practice.py`:

```python
name = input("Name: ")
print(type(name))
print(name)

age = input("Age: ")
print(type(age))

age = int(age)
print(type(age))
print(age >= 18)

current_number = 0

while current_number < 5:
    current_number += 1
    print(current_number)

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)
```

## Beginner rule to extract

```text
input() always returns a string.
Use int() when the input should behave like a number.
Use while when the loop should continue until a condition changes.
Use break when a specific input should exit the loop immediately.
Use continue when one loop iteration should be skipped.
```

---

# Common Mistakes to Watch For

## Forgetting That `input()` Returns a String

Incorrect:

```python
age = input("How old are you? ")

if age >= 18:
    print("You can vote.")
```

This causes a type error because `age` is a string.

Correct:

```python
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You can vote.")
```

---

## Converting `"quit"` with `int()`

Incorrect:

```python
age = input("Enter your age, or 'quit': ")
age = int(age)

if age == "quit":
    print("Goodbye.")
```

This fails if the user enters `"quit"` because `"quit"` cannot be converted to an integer.

Correct:

```python
age = input("Enter your age, or 'quit': ")

if age == "quit":
    print("Goodbye.")
else:
    age = int(age)
```

---

## Forgetting to Change the Loop Condition

Incorrect:

```python
current_number = 1

while current_number <= 5:
    print(current_number)
```

This loop never changes `current_number`, so it never ends.

Correct:

```python
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
```

---

## Printing the Quit Value

Less clean:

```python
message = ""

while message != "quit":
    message = input("Enter a message: ")
    print(message)
```

This prints `"quit"` before stopping.

Cleaner:

```python
message = ""

while message != "quit":
    message = input("Enter a message: ")

    if message != "quit":
        print(message)
```

---

## Using `if` Instead of `while` to Remove All Values

Incorrect:

```python
pets = ["cat", "dog", "cat"]

if "cat" in pets:
    pets.remove("cat")
```

This removes only one `"cat"`.

Correct:

```python
pets = ["cat", "dog", "cat"]

while "cat" in pets:
    pets.remove("cat")
```

---

## Creating an Infinite Loop by Accident

Incorrect:

```python
active = True

while active:
    print("Running...")
```

This never changes `active`.

Correct:

```python
active = True

while active:
    answer = input("Type 'quit' to stop: ")

    if answer == "quit":
        active = False
```

---

# Suggested Workflow

For each exercise:

1. Read the task.
2. Identify whether the input is text or a number.
3. If it is a number, decide where to use `int()`.
4. Decide how the loop should stop.
5. Predict what should happen before running the file.
6. Write the code.
7. Run the file.
8. Test the normal case.
9. Test the quit/stop case.
10. Fix syntax or logic errors.
11. Improve output formatting.
12. Commit after a meaningful group of exercises.

Run an exercise:

```bash
python3 python/python-crash-course/chapter-07-user-input-and-while-loops-exercises/exercise_7_1_rental_car.py
```

Suggested commits:

```bash
git add .
git commit -m "Complete Chapter 7 input exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 7 while loop exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 7 list processing exercises"
git push
```

```bash
git add .
git commit -m "Add Chapter 7 notes and docs practice"
git push
```
```bash
git add .
git commit -m "Add Chapter 7 README"
git push
```

---

# Chapter 7 Completion Checklist

Mark each exercise when completed.

- [ ] 7-1 Rental Car
- [ ] 7-2 Restaurant Seating
- [ ] 7-3 Multiples of Ten
- [ ] 7-4 Pizza Toppings
- [ ] 7-5 Movie Tickets
- [ ] 7-6 Three Exits
- [ ] 7-7 Infinity
- [ ] 7-8 Deli
- [ ] 7-9 No Pastrami
- [ ] 7-10 Dream Vacation

---

# Self-Review Questions

Answer these after finishing the chapter.

## User Input

1. What does `input()` do?
- `input()` pauses the program, displays a prompt, waits for the user to type something, and returns what the user typed.

2. What type does `input()` return?
- `input()` always returns a string.

3. Why does `input()` return a string even when the user types a number?
- Python receives keyboard input as text.
- If the program needs numeric behavior, the string must be converted with a function such as `int()` or `float()`.

4. When should I use `int()`?
- Use `int()` when a value should behave like a whole number.
- This is especially important before arithmetic, numeric comparisons, or modulo checks.

5. What can go wrong if I call `int()` on `"quit"`?
- Python raises a `ValueError` because `"quit"` is not valid integer text.

---

## Numerical Input

6. Why does `age >= 18` fail if `age` is still a string?
- It tries to compare a string with an integer.
- Python does not know how to order those two different types in that comparison.

7. What does `%` do?
- `%` returns the remainder after division.

8. How do I check whether a number is a multiple of `10`?
- Check whether the number divided by `10` leaves a remainder of `0`.

9. How do I check whether a number is even?
- Check whether the number divided by `2` leaves a remainder of `0`.

---

## while Loops

10. What does a `while` loop do?
- A `while` loop repeats a block of code as long as its condition is true.

11. How is a `while` loop different from a `for` loop?
- A `for` loop is usually used when iterating through a known sequence.
- A `while` loop is used when repetition depends on a condition that can change.

12. What must usually change inside a `while` loop?
- Some value involved in the loop condition must usually change.
- If nothing changes, the loop may never stop.

13. What causes an infinite loop?
- An infinite loop happens when the loop condition never becomes false and no `break` exits the loop.

14. How do I stop a running infinite loop in the terminal?
- Press `CTRL-C`.

---

## Loop Control

15. What does `break` do?
- `break` exits the nearest enclosing loop immediately.

16. What does `continue` do?
- `continue` skips the rest of the current loop iteration and moves to the next iteration.

17. What is an active variable?
- An active variable is usually a boolean flag that controls whether a loop should keep running.

18. When is `while True` readable?
- `while True` is readable when the loop has a clear exit path.
- Usually this means there is a clear `break` statement triggered by a specific condition.

19. When should I use a sentinel value like `"quit"`?
- Use a sentinel value when the user needs a clear input that means “stop the loop.”

---

## Lists and Dictionaries with while Loops

20. Why does `while sandwich_orders:` stop when the list is empty?
- Non-empty lists are truthy.
- Empty lists are falsey.
- When all items have been removed, the list becomes falsey and the loop stops.

21. What does `.pop()` do?
- `.pop()` removes and returns an item from a list.
- Without an index, it removes and returns the last item.

22. What does `.append()` do?
- `.append()` adds one item to the end of a list.
- It mutates the original list.

23. Why does `while "pastrami" in sandwich_orders:` remove all pastrami orders?
- The loop keeps running while at least one `"pastrami"` remains.
- Each iteration removes one matching value.
- Eventually, all matching values are removed.

24. How can a `while` loop fill a dictionary with user input?
- Each loop iteration can collect a key and value from the user.
- The program can then assign that key-value pair into the dictionary.

---

## Style and Review

25. Why should prompts include a space at the end?
- A trailing space separates the prompt text from the user’s typed input.
- This makes the terminal interaction easier to read.

26. Why should output messages be readable?
- Readable messages make the program easier to use, test, and debug.

27. Why should I test the quit path?
- The quit path controls how the loop stops.
- If it is broken, the program may crash, print unwanted output, or loop forever.

28. Which JavaScript habits should I avoid when writing Python input and loops?
- Avoid braces for blocks.
- Avoid `let` and `const`.
- Avoid JavaScript-style template literals.
- Avoid relying on truthiness without understanding Python’s rules.
- Use indentation, f-strings, Python boolean values, and Python loop syntax.

---

# Key Takeaways

- `input()` pauses the program and returns user input as a string.
- Use `int()` when you need numeric comparison.
- Use `%` to check divisibility.
- A `while` loop repeats while its condition is true.
- A `for` loop is usually best when looping through a known collection.
- A `while` loop is useful when the loop depends on user input or changing state.
- `break` exits a loop immediately.
- `continue` skips the rest of the current loop iteration.
- An active variable can control whether a loop keeps running.
- `while True` is readable when there is a clear `break`.
- Empty lists evaluate to `False`.
- `while list_name:` can process a list until it is empty.
- `while value in list_name:` can remove all occurrences of a value.
- `.pop()` removes and returns an item.
- `.append()` adds an item to the end of a list.
- A dictionary can be filled with user responses during a loop.
- Always test the normal path and the quit path.
