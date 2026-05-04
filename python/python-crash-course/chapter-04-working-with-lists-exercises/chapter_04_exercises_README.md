# Python Crash Course — Chapter 4 Exercises

## Chapter 4 — Working with Lists

This folder contains practice exercises for **Python Crash Course Chapter 4: Working with Lists**.

The goal of this chapter is to learn how to:

- loop through a list with a `for` loop
- understand loop variables
- use indentation correctly
- avoid common indentation errors
- use `range()`
- create number lists with `list(range())`
- use `min()`, `max()`, and `sum()`
- create lists with loops and `append()`
- create lists with list comprehensions
- slice lists
- loop through slices
- copy lists correctly
- define and use tuples
- understand immutable values
- write cleaner Python using PEP 8 style guidelines

Recommended folder:

```text
python/python-crash-course/chapter-04-working-with-lists
```

Recommended file names:

```text
dimensions.py
even_numbers.py
first_numbers.py
foods.py
magicians.py
players.py
square_numbers.py
squares.py
```
Exercise file names:

```text
exercise_4_1_pizzas.py
exercise_4_2_animals.py
exercise_4_3_counting_to_twenty.py
exercise_4_4_one_million.py
exercise_4_5_summing_a_million.py
exercise_4_6_odd_numbers.py
exercise_4_7_threes.py
exercise_4_8_cubes.py
exercise_4_9_cube_comprehension.py
exercise_4_10_slices.py
exercise_4_11_my_pizzas_your_pizzas.py
exercise_4_12_more_loops.py
exercise_4_13_buffet.py
```

---

# Example — Looping Through a List

## Task

Create a list of magicians and use a `for` loop to print each name.

## Concepts

- lists
- `for` loops
- loop variables
- indentation

## Starter code

```python
magicians = ["alice", "david", "carolina"]
```

<details>
<summary>Show starter code</summary>

```python
for magician in magicians:
    print(magician)
```

</details>

## Goal

Understand how Python repeats the same action once for each item in a list.

---

# Example — Doing More Work in a Loop

## Task

Use a `for` loop to print two messages for each magician.

## Concepts

- multiple indented lines
- f-strings
- code inside a loop

## Starter code

```python
magicians = ["alice", "david", "carolina"]
```

<details>
<summary>Show starter code</summary>

```python
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

</details>

## Goal

Understand that every indented line after the `for` statement runs once for each item.

---

# Example — Doing Something After a Loop

## Task

Print a personal message for each magician, then print one group message after the loop.

## Concepts

- code inside a loop
- code outside a loop
- indentation

## Starter code

```python
magicians = ["alice", "david", "carolina"]
```

<details>
<summary>Show starter code</summary>

```python
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
```

</details>

## Goal

Learn that unindented code after a loop runs once, after the loop is finished.

---

# Exercise 4-1 — Pizzas

## Task

Think of at least three kinds of your favorite pizza.

Store these pizza names in a list, and then use a `for` loop to print the name of each pizza.

Then:

1. Modify your loop to print a sentence using the name of each pizza.
2. Add a line outside the loop that states how much you like pizza.

## Concepts

- lists
- `for` loops
- loop variables
- f-strings
- code after a loop

## Starter code

```python
pizzas = ["margherita", "pepperoni", "vegetarian"]
```

<details>
<summary>Show starter code</summary>

```python
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")
```

</details>

## Goal

Practice looping through every item in a list and running the same action for each item.

---

# Exercise 4-2 — Animals

## Task

Think of at least three animals that have a common characteristic.

Store the names of these animals in a list, and then use a `for` loop to print the name of each animal.

Then:

1. Modify your program to print a statement about each animal.
2. Add a line outside the loop stating what these animals have in common.

## Concepts

- lists
- `for` loops
- f-strings
- summary after a loop

## Starter code

```python
animals = ["dog", "cat", "rabbit"]
```

<details>
<summary>Show starter code</summary>

```python
for animal in animals:
    print(f"A {animal} would make a great pet.")

print("Any of these animals would make a great pet!")
```

</details>

## Goal

Practice using singular and plural names clearly in loops.

---

# Exercise 4-3 — Counting to Twenty

## Task

Use a `for` loop to print the numbers from `1` to `20`, inclusive.

## Concepts

- `for` loops
- `range()`
- inclusive vs exclusive end values

## Starter code

```python
# Print the numbers from 1 to 20.
```

<details>
<summary>Show starter code</summary>

```python
for number in range(1, 21):
    print(number)
```

</details>

## Goal

Understand that the stop value in `range()` is not included.

---

# Exercise 4-4 — One Million

## Task

Make a list of the numbers from `1` to `1_000_000`.

Then use a `for` loop to print the numbers.

If the output takes too long, stop it with `CTRL-C`.

## Concepts

- large ranges
- number lists
- `list(range())`
- performance awareness

## Starter code

```python
numbers = list(range(1, 1_000_001))
```

<details>
<summary>Show starter code</summary>

```python
for number in numbers:
    print(number)
```

</details>

## Goal

Understand that Python can work with very large lists, but printing huge output can be slow.

---

# Exercise 4-5 — Summing a Million

## Task

Make a list of the numbers from `1` to `1_000_000`.

Then use:

- `min()`
- `max()`
- `sum()`

to check the smallest value, largest value, and total.

## Concepts

- `list(range())`
- `min()`
- `max()`
- `sum()`

## Starter code

```python
numbers = list(range(1, 1_000_001))
```

<details>
<summary>Show starter code</summary>

```python
print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

</details>

## Goal

Practice simple statistics with a list of numbers.

---

# Exercise 4-6 — Odd Numbers

## Task

Use the third argument of `range()` to make a list of the odd numbers from `1` to `20`.

Use a `for` loop to print each number.

## Concepts

- `range(start, stop, step)`
- odd numbers
- loops

## Starter code

```python
odd_numbers = list(range(1, 20, 2))
```

<details>
<summary>Show starter code</summary>

```python
for number in odd_numbers:
    print(number)
```

</details>

## Goal

Practice using the step argument in `range()`.

---

# Exercise 4-7 — Threes

## Task

Make a list of the multiples of `3`, from `3` to `30`.

Use a `for` loop to print the numbers in your list.

## Concepts

- `range()`
- step values
- multiples

## Starter code

```python
threes = list(range(3, 31, 3))
```

<details>
<summary>Show starter code</summary>

```python
for number in threes:
    print(number)
```

</details>

## Goal

Practice creating a numeric sequence with a step value.

---

# Exercise 4-8 — Cubes

## Task

A number raised to the third power is called a cube.

Make a list of the first 10 cubes.

Use a `for` loop to print each cube.

## Concepts

- exponentiation with `**`
- loops
- `append()`
- number lists

## Starter code

```python
cubes = []
```

<details>
<summary>Show starter code</summary>

```python
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)
```

</details>

## Goal

Practice building a list with a loop and `append()`.

---

# Exercise 4-9 — Cube Comprehension

## Task

Use a list comprehension to generate a list of the first 10 cubes.

## Concepts

- list comprehensions
- exponentiation
- `range()`

## Starter code

```python
# Create the first 10 cubes with a list comprehension.
```

<details>
<summary>Show starter code</summary>

```python
cubes = [number ** 3 for number in range(1, 11)]

print(cubes)
```

</details>

## Goal

Practice rewriting a loop-and-append pattern as a list comprehension.

---

# Exercise 4-10 — Slices

## Task

Using one of the programs you wrote in this chapter, add several lines that do the following:

1. Print the message `The first three items in the list are:`
2. Use a slice to print the first three items.
3. Print the message `Three items from the middle of the list are:`
4. Use a slice to print three items from the middle.
5. Print the message `The last three items in the list are:`
6. Use a slice to print the last three items.

## Concepts

- slicing
- start index
- stop index
- negative slices

## Starter code

```python
players = ["charles", "martina", "michael", "florence", "eli"]
```

<details>
<summary>Show starter code</summary>

```python
print("The first three items in the list are:")
print(players[:3])

print("Three items from the middle of the list are:")
print(players[1:4])

print("The last three items in the list are:")
print(players[-3:])
```

</details>

## Goal

Practice working with part of a list.

---

# Exercise 4-11 — My Pizzas, Your Pizzas

## Task

Start with your program from Exercise 4-1.

Make a copy of the list of pizzas and call it `friend_pizzas`.

Then:

1. Add a new pizza to the original list.
2. Add a different pizza to `friend_pizzas`.
3. Prove that you have two separate lists.
4. Print both lists with `for` loops.

## Concepts

- copying lists
- slicing with `[:]`
- separate lists vs same list reference
- `for` loops

## Starter code

```python
pizzas = ["margherita", "pepperoni", "vegetarian"]
friend_pizzas = pizzas[:]
```

<details>
<summary>Show starter code</summary>

```python
pizzas.append("hawaiian")
friend_pizzas.append("mushroom")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
```

</details>

## Goal

Understand how to copy a list correctly using a full slice.

---

# Exercise 4-12 — More Loops

## Task

Choose one version of `foods.py`.

Write two `for` loops to print each list of foods.

## Concepts

- lists
- copying lists
- `for` loops

## Starter code

```python
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
```

<details>
<summary>Show starter code</summary>

```python
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
```

</details>

## Goal

Practice using loops instead of printing entire lists directly.

---

# Exercise 4-13 — Buffet

## Task

A buffet-style restaurant offers only five basic foods.

Store the foods in a tuple.

Then:

1. Use a `for` loop to print each food.
2. Try to modify one item and confirm that Python rejects the change.
3. Rewrite the tuple with two different foods.
4. Use a `for` loop to print the revised menu.

## Concepts

- tuples
- immutability
- looping through tuples
- reassigning a tuple

## Starter code

```python
foods = ("rice", "beans", "salad", "soup", "bread")
```

<details>
<summary>Show starter code</summary>

```python
for food in foods:
    print(food)

# This should raise a TypeError if uncommented:
# foods[0] = "pasta"

foods = ("pasta", "beans", "salad", "fish", "bread")

print("\nRevised menu:")
for food in foods:
    print(food)
```

</details>

## Goal

Understand that tuples cannot be modified item by item, but the variable can be reassigned to a new tuple.

---

# Exercise 4-14 — PEP 8

## Task

Read or skim the original PEP 8 style guide.

You will not use all of it yet, but you should start noticing the main style rules.

## Concepts

- code style
- readability
- indentation
- line length
- blank lines

## Starter code

```text
PEP 8: https://peps.python.org/pep-0008/
```

<details>
<summary>Show starter code</summary>

```text
Focus on:
- 4 spaces per indentation level
- clear variable names
- reasonable line length
- not using excessive blank lines
```

</details>

## Goal

Understand that professional Python code follows shared readability conventions.

---

# Exercise 4-15 — Code Review

## Task

Choose three programs you wrote in this chapter and modify each one to follow PEP 8.

Check:

1. Four spaces per indentation level.
2. Lines are not too long.
3. Blank lines are not excessive.
4. Variable names are clear.
5. Output messages are readable.

## Concepts

- refactoring
- style review
- readable code
- professional habits

## Starter code

```text
Choose three files from Chapter 4.
```

<details>
<summary>Show starter code</summary>

```text
Recommended files:
- pizzas.py
- cubes.py
- buffet.py
```

</details>

## Goal

Practice reviewing and improving code after it already works.

---

# Common Mistakes to Watch For

## Forgetting to Indent

Incorrect:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
print(magician)
```

Correct:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)
```

---

## Forgetting to Indent Additional Lines

Incorrect:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

The second message runs only once after the loop.

Correct:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

---

## Indenting After the Loop by Accident

Incorrect:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print("Thank you, everyone.")
```

`"Thank you, everyone."` runs once for each magician.

Correct:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("Thank you, everyone.")
```

---

## Forgetting the Colon

Incorrect:

```python
for magician in magicians
    print(magician)
```

Correct:

```python
for magician in magicians:
    print(magician)
```

---

## Forgetting That `range()` Stops Before the End

```python
for number in range(1, 5):
    print(number)
```

This prints:

```text
1
2
3
4
```

To include `5`, use:

```python
for number in range(1, 6):
    print(number)
```

---

## Copying a List Incorrectly

Incorrect:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods
```

Both variables point to the same list.

Correct:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
```

This creates a separate copy.

---

# Suggested Workflow

For each exercise:

1. Read the task.
2. Write the code from memory.
3. Run the file.
4. Fix errors.
5. Add a short comment explaining the main concept if useful.
6. Review indentation carefully.
7. Commit after a meaningful group of exercises.

Example:

```bash
python3 python/python-crash-course/chapter-04-working-with-lists/pizzas.py
```

Commit examples:

```bash
git add .
git commit -m "Complete Chapter 4 loop exercises"
git push
```

```bash
git add .
git commit -m "Practice range and number lists"
git push
```

```bash
git add .
git commit -m "Complete Chapter 4 slicing and tuple exercises"
git push
```

```bash
git add .
git commit -m "Refactor Chapter 4 exercises for PEP 8"
git push
```

---

# Chapter 4 Completion Checklist

Mark each exercise when completed.

- [ ] 4-1 Pizzas
- [ ] 4-2 Animals
- [ ] 4-3 Counting to Twenty
- [ ] 4-4 One Million
- [ ] 4-5 Summing a Million
- [ ] 4-6 Odd Numbers
- [ ] 4-7 Threes
- [ ] 4-8 Cubes
- [ ] 4-9 Cube Comprehension
- [ ] 4-10 Slices
- [ ] 4-11 My Pizzas, Your Pizzas
- [ ] 4-12 More Loops
- [ ] 4-13 Buffet
- [ ] 4-14 PEP 8
- [ ] 4-15 Code Review

---

# Self-Review Questions

Answer these after finishing the chapter.

## Loops

1. What does a `for` loop do?
2. What is the loop variable?
3. Why does indentation matter in a loop?
4. How do I know which code is inside the loop?
5. What happens to unindented code after a loop?

## Numerical Lists

6. What does `range(1, 5)` produce?
7. Why do I use `range(1, 21)` to print 1 through 20?
8. What does the third argument in `range(start, stop, step)` do?
9. What does `list(range(1, 6))` return?
10. What do `min()`, `max()`, and `sum()` do?

## List Comprehensions

11. What is a list comprehension?
12. When might I use a list comprehension instead of a normal loop?
13. Why should I write the normal loop first if I am confused?

## Slices and Copies

14. What does `players[0:3]` return?
15. What does `players[:3]` return?
16. What does `players[-3:]` return?
17. How do I copy a list correctly?
18. What happens if I use `friend_foods = my_foods` instead of `friend_foods = my_foods[:]`?

## Tuples

19. What is a tuple?
20. How is a tuple different from a list?
21. Can I modify one item inside a tuple?
22. Can I reassign a variable to a new tuple?

## Style

23. Why does PEP 8 recommend four spaces for indentation?
24. Why should code be easy to read?
25. What should I check during a code review?

---

# Key Takeaways

- A `for` loop lets you repeat work for every item in a list.
- The loop variable represents one item at a time.
- Indentation controls what belongs inside the loop.
- Unindented code after a loop runs once after the loop finishes.
- `range()` generates numbers but does not include the stop value.
- `list(range())` creates a list of numbers.
- `min()`, `max()`, and `sum()` help summarize numeric lists.
- List comprehensions create lists in a compact way.
- Slices let you work with part of a list.
- `[:]` creates a copy of a list.
- Assigning one list variable to another does not create a copy.
- Tuples are ordered collections that cannot be modified item by item.
- PEP 8 helps keep Python code readable.
