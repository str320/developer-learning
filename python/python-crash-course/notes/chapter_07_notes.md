# Chapter 7 Notes — User Input and While Loops

These notes summarize the most important ideas from **Python Crash Course Chapter 7: User Input and While Loops**.

This is the **GitHub version** of the notes. It is meant to live near the runnable Chapter 7 exercise files.

Recommended location:

```text
python/python-crash-course/chapter-07-user-input-and-while-loops-exercises/notes.md
```

---

## What Chapter 7 Is About

Chapter 7 introduces programs that respond to user input and repeat actions while a condition remains true.

You learned how to:

```text
- use input() to ask the user for information
- understand that input() returns a string
- convert input with int()
- use modulo % to check divisibility
- write while loops
- stop while loops with a condition
- use an active flag to control a loop
- use break to exit a loop immediately
- use continue to skip the rest of one loop cycle
- move items from one list to another
- remove repeated values from a list
- fill a dictionary with user input
- format interactive program output clearly
```

---

## User Input

`input()` pauses the program and waits for the user to type something.

Example:

```python
name = input("Please enter your name: ")
print(f"Hello, {name}!")
```

The prompt is the message shown to the user.

```text
"Please enter your name: " is the prompt.
```

The value typed by the user is stored in the variable.

Important rule:

```text
input() always returns a string.
```

Even if the user types a number, Python receives it as text first.

---

## Writing Clear Prompts

A prompt should tell the user exactly what to enter.

Example:

```python
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car.title()}.")
```

Good prompts are:

```text
- clear
- specific
- friendly
- followed by a space when the user will type after the prompt
```

Less clear:

```python
car = input("Car")
```

Clearer:

```python
car = input("What kind of rental car would you like? ")
```

---

## Multi-Line Prompts

You can build a longer prompt with multiple strings.

Example:

```python
prompt = "If you tell us who you are, we can personalize your message."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name.title()}!")
```

This is useful when the prompt needs more explanation.

The `+=` operator adds more text to the existing string.

---

## Converting Input with `int()`

Because `input()` returns a string, numeric input must be converted before numeric comparison.

Example:

```python
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are too young to vote.")
```

Without `int()`, this comparison would be incorrect because Python would be comparing a string to an integer.

Incorrect:

```python
age = input("How old are you? ")

if age >= 18:
    print("You are old enough to vote.")
```

Correct:

```python
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You are old enough to vote.")
```

---

## Using `%` for Multiples

The modulo operator `%` returns the remainder after division.

Example:

```python
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
```

If the remainder is `0`, the number divides evenly.

Examples:

```text
20 % 10 == 0
25 % 10 == 5
```

Use `%` when you need to check:

```text
- even or odd
- divisibility
- multiples
- repeated cycles later in programming
```

---

## While Loops

A `while` loop repeats as long as its condition is `True`.

Example:

```python
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
```

Output:

```text
1
2
3
4
5
```

The loop needs a condition that eventually becomes false.

In this example:

```python
current_number += 1
```

moves the loop toward stopping.

---

## Avoiding Infinite Loops

A loop becomes infinite if its stopping condition never becomes false.

Incorrect:

```python
current_number = 1

while current_number <= 5:
    print(current_number)
```

This never changes `current_number`, so the loop never stops.

Correct:

```python
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
```

If you accidentally create an infinite loop in the terminal, stop it with:

```text
CTRL-C
```

---

## Letting the User Quit

Interactive programs often keep running until the user enters a quit value.

Example:

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)
```

This loop continues until the user types `quit`.

Important detail:

```text
The program checks the value of message each time the loop starts.
```

---

## Using an Active Flag

A flag is a variable that controls whether a loop should keep running.

Example:

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)
```

The flag is useful when several different conditions might stop the loop.

In this example:

```python
active = False
```

causes the loop to stop the next time Python checks the `while active:` condition.

---

## Using `break`

`break` exits a loop immediately.

Example:

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

`while True` creates a loop that would normally run forever.

The `break` statement gives the loop a clear exit.

Use `break` when:

```text
- you want a direct exit
- the stopping condition is checked inside the loop
- the loop should stop immediately
```

---

## Using `continue`

`continue` skips the rest of the current loop cycle and starts the next cycle.

Example:

```python
current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)
```

Output:

```text
1
3
5
7
9
```

When the number is even, `continue` skips the `print()` line.

Use `continue` when:

```text
- one case should be skipped
- the loop should keep running
- the current item should not be processed
```

---

## Three Ways to Stop a Loop

Chapter 7 shows three common loop exits.

### 1. Conditional test in the `while` statement

```python
message = ""

while message != "quit":
    message = input("Enter a message or 'quit': ")
```

### 2. Active flag

```python
active = True

while active:
    message = input("Enter a message or 'quit': ")

    if message == "quit":
        active = False
```

### 3. `break`

```python
while True:
    message = input("Enter a message or 'quit': ")

    if message == "quit":
        break
```

All three are valid. Choose the one that makes the loop easiest to understand.

---

## Moving Items from One List to Another

A `while` loop can process items until a list is empty.

Example:

```python
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

Important pattern:

```python
while unconfirmed_users:
```

This means:

```text
Keep looping while the list still has items.
```

An empty list evaluates to `False`, so the loop stops when the list is empty.

This combines:

```text
- while loops
- truth value testing
- list.pop()
- list.append()
- for loops
```

---

## Removing All Instances of a Value

`remove()` removes one matching value at a time.

Use a `while` loop to remove all matching values.

Example:

```python
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]

while "cat" in pets:
    pets.remove("cat")

print(pets)
```

Result:

```python
["dog", "dog", "goldfish", "rabbit"]
```

This pattern is useful when a list may contain repeated unwanted values.

---

## Filling a Dictionary with User Input

You can use a loop to collect responses and store them in a dictionary.

Example:

```python
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
```

This combines Chapter 6 and Chapter 7:

```text
- dictionaries
- key-value pairs
- user input
- while loops
- flags
- .items()
```

---

## Case-Insensitive User Responses

User input may have different capitalization.

Example:

```python
repeat = input("Would you like to continue? (yes/no) ")

if repeat.lower() == "no":
    active = False
```

This handles:

```text
no
No
NO
nO
```

Use `.lower()` when capitalization should not matter.

---

## Common Mistakes

### Forgetting that `input()` returns a string

Incorrect:

```python
age = input("How old are you? ")

if age >= 18:
    print("You can vote.")
```

Correct:

```python
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You can vote.")
```

---

### Creating a prompt string but forgetting `input()`

Incorrect:

```python
name = "Please enter your name: "
print(f"Hello, {name}!")
```

This stores the prompt text itself in `name`.

Correct:

```python
name = input("Please enter your name: ")
print(f"Hello, {name}!")
```

---

### Forgetting to update the loop variable

Incorrect:

```python
current_number = 1

while current_number <= 5:
    print(current_number)
```

Correct:

```python
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
```

---

### Printing the quit value

Incorrect:

```python
message = ""

while message != "quit":
    message = input("Enter a message: ")
    print(message)
```

If the user types `quit`, the program prints `quit` before stopping.

Correct:

```python
message = ""

while message != "quit":
    message = input("Enter a message: ")

    if message != "quit":
        print(message)
```

---

### Using `continue` before updating the loop variable

Incorrect:

```python
current_number = 0

while current_number < 10:
    if current_number % 2 == 0:
        continue

    current_number += 1
    print(current_number)
```

This can create an infinite loop because `continue` skips the update.

Correct:

```python
current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)
```

---

### Removing only one repeated value

Incorrect if you want to remove all cats:

```python
pets = ["dog", "cat", "cat", "rabbit"]
pets.remove("cat")
```

Correct:

```python
pets = ["dog", "cat", "cat", "rabbit"]

while "cat" in pets:
    pets.remove("cat")
```

---

### Forgetting to append processed items

Incorrect:

```python
sandwich_orders = ["tuna", "turkey", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
```

This removes the order but does not store it in `finished_sandwiches`.

Correct:

```python
sandwich_orders = ["tuna", "turkey", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
```

---

## Official Docs Practice

Chapter 7 connects to these Python documentation topics:

```text
input()
int()
while statements
break
continue
truth value testing
list.pop()
list.append()
list.remove()
dict.items()
```

### Official Reading Links

Read only these sections from the Python official documentation:

- [Built-in Functions — input()](https://docs.python.org/3/library/functions.html#input)
- [Built-in Functions — int()](https://docs.python.org/3/library/functions.html#int)
- [The while statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- [The break statement](https://docs.python.org/3/reference/simple_stmts.html#the-break-statement)
- [The continue statement](https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement)
- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

When reading documentation, ask:

```text
1. What problem does this feature solve?
2. What syntax does it use?
3. What does it return?
4. Does it mutate the original object?
5. Can it raise an error?
6. Can I run one tiny example?
7. What mistake should I avoid?
```

### Small Experiments

Add these to `docs_practice.py` or test them in a temporary file.

```python
name = input("Name: ")
print(name)
print(type(name))
```

```python
age = input("Age: ")
age = int(age)
print(age >= 18)
```

```python
number = 0

while number < 5:
    number += 1
    print(number)
```

```python
number = 0

while number < 10:
    number += 1

    if number % 2 == 0:
        continue

    print(number)
```

```python
items = ["a", "b", "c"]

while items:
    item = items.pop()
    print(item)

print(items)
```

```python
pets = ["cat", "dog", "cat"]

while "cat" in pets:
    pets.remove("cat")

print(pets)
```

### Beginner Rules to Extract

```text
input() returns a string.
Use int() before numeric comparison.
A while loop repeats while its condition is true.
break exits the loop immediately.
continue skips to the next loop cycle.
An empty list is false in a condition.
Use while item in list when you need to remove all matching values.
Use a dictionary to store poll responses by name.
```

---

## Key Corrections from Chapter 7

### Convert numeric input before comparison

This is risky:

```python
age = input("Age: ")

if age >= 18:
    print("Adult")
```

Use this:

```python
age = input("Age: ")
age = int(age)

if age >= 18:
    print("Adult")
```

---

### Use `while True` only with a clear exit

This is risky:

```python
while True:
    city = input("City: ")
    print(city)
```

Better:

```python
while True:
    city = input("City or 'quit': ")

    if city == "quit":
        break

    print(city)
```

---

### Put loop updates before `continue`

This is risky:

```python
while number < 10:
    if number % 2 == 0:
        continue

    number += 1
```

Better:

```python
while number < 10:
    number += 1

    if number % 2 == 0:
        continue
```

---

### Use `while list_name:` when processing all items

Less direct:

```python
while len(unconfirmed_users) > 0:
    current_user = unconfirmed_users.pop()
```

More Pythonic:

```python
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
```

---

### Use `.lower()` for yes/no input

Less safe:

```python
if repeat == "no":
    active = False
```

More flexible:

```python
if repeat.lower() == "no":
    active = False
```

---

## Code Review Checklist

When reviewing Chapter 7 code, check:

```text
- Did I use input() when I need user input?
- Is the prompt clear and readable?
- Did I remember that input() returns a string?
- Did I convert numeric input with int() before comparing numbers?
- Could invalid input cause a ValueError?
- Does every while loop have a clear stopping condition?
- Did I avoid accidental infinite loops?
- Did I use break only when it makes the loop clearer?
- Did I use continue only when skipping one loop cycle is clearer?
- If I used continue, does the loop variable still update?
- Did I avoid printing the quit value?
- Did I use while list_name: when processing a list until empty?
- Did I append processed items to the finished list when needed?
- Did I use while item in list when removing all repeated values?
- Did I use .items() when printing dictionary poll results?
- Did I use .lower() when yes/no capitalization should not matter?
- Is the output readable for a human?
```

---

## Chapter 7 Exercises Practiced

Mark each exercise when completed.

```text
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
```

---

## Review Questions

1. What does `input()` do?
2. What type does `input()` return?
3. Why do you need `int()` before comparing numeric user input?
4. What does the modulo operator `%` return?
5. How do you check whether a number is a multiple of 10?
6. What is a `while` loop?
7. How is a `while` loop different from a `for` loop?
8. What can cause an infinite loop?
9. How do you stop a program that is stuck in an infinite loop?
10. What is an active flag?
11. When should you use `break`?
12. When should you use `continue`?
13. Why should you be careful using `continue` before updating a loop variable?
14. What does `while unconfirmed_users:` mean?
15. Why does an empty list stop the loop?
16. Why does `remove()` need a `while` loop when removing all repeated values?
17. How do you move an item from one list to another?
18. How do you fill a dictionary with user input?
19. Why might `.lower()` be useful with yes/no answers?
20. Which Chapter 7 patterns will be useful later in Django forms or user workflows?

---

## Key Takeaways

- `input()` lets the user enter information while the program runs.
- `input()` always returns a string.
- Use `int()` when input needs to become a number.
- `%` helps check divisibility and multiples.
- A `while` loop repeats while a condition is true.
- A loop needs a clear way to stop.
- `break` exits a loop immediately.
- `continue` skips the rest of one loop cycle.
- An empty list evaluates to `False`.
- `while list_name:` is useful for processing a list until it is empty.
- `while item in list:` is useful for removing all repeated values.
- User input can be stored in dictionaries.
- `.lower()` makes yes/no input more flexible.
- Chapter 7 connects user interaction, loops, lists, and dictionaries.
- These patterns matter later for Django forms, validation, and user workflows.

---

## Suggested Git Workflow

After finishing the Chapter 7 exercises:

```bash
git status
git add .
git commit -m "Complete Chapter 7 input and while loop exercises"
git push
```

If you add docs practice separately:

```bash
git status
git add .
git commit -m "Add Chapter 7 docs practice notes"
git push
```
