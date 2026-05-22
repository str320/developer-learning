# Chapter 4 Notes — Working with Lists

These notes summarize the most important ideas from **Python Crash Course Chapter 4: Working with Lists**.

Use this file for chapter-specific review. The main exercise instructions and checklist stay in `README.md`.

---

## For Loops

A `for` loop repeats code once for each item in a sequence.

Example:

```python
pizzas = ["margherita", "pepperoni", "vegetarian"]

for pizza in pizzas:
    print(pizza)
```

The loop reads like this:

```text
For each pizza in the list of pizzas, print the pizza.
```

The list is usually plural:

```python
pizzas = ["margherita", "pepperoni", "vegetarian"]
```

The loop variable is usually singular:

```python
for pizza in pizzas:
```

## Loop Variables

The loop variable temporarily stores the current item during each pass through the loop.

Example:

```python
animals = ["dog", "cat", "rabbit"]

for animal in animals:
    print(animal)
```

During the loop, Python behaves like this:

```text
animal = "dog"
animal = "cat"
animal = "rabbit"
```

The loop variable changes automatically each time the loop runs.

---

## Indentation

Python uses indentation to decide which lines belong inside a loop.

This code runs both `print()` calls for every item:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!")
```

This code runs the final `print()` only once after the loop:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("Thank you, everyone.")
```

### Rule

```text
Indented = inside the loop
Not indented = outside the loop
```

---

## Common Loop Mistakes

### Forgetting to indent

Incorrect:

```python
for magician in magicians:
print(magician)
```

Correct:

```python
for magician in magicians:
    print(magician)
```

### Indenting too much

Incorrect:

```python
for magician in magicians:
    print(magician)
    print("Thank you, everyone.")
```

If the thank-you message should happen once, move it outside the loop:

```python
for magician in magicians:
    print(magician)

print("Thank you, everyone.")
```

### Forgetting the colon

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

## `range()`

`range()` creates a sequence of numbers.

Example:

```python
for number in range(1, 5):
    print(number)
```

Output:

```text
1
2
3
4
```

The stop value is not included.

So:

```python
range(1, 5)
```

produces:

```text
1, 2, 3, 4
```

To print `1` through `20`, use:

```python
for number in range(1, 21):
    print(number)
```

Because `21` is excluded, the last printed number is `20`.

---

## `range(start, stop, step)`

The third argument controls the step.

Example:

```python
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)
```

Output:

```text
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

Example with multiples of 3:

```python
threes = list(range(3, 31, 3))
print(threes)
```

Output:

```text
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

---

## Numerical Lists

Use `list(range())` to create a list of numbers.

Example:

```python
numbers = list(range(1, 6))
print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

Useful functions for numerical lists:

```python
numbers = [1, 2, 3, 4, 5]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

Result:

```text
1
5
15
```

### What They Do

```text
min() returns the smallest value.
max() returns the largest value.
sum() adds all the values.
```

---

## Building a List with a Loop

You can start with an empty list and add values with `.append()`.

Example:

```python
cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

print(cubes)
```

Output:

```text
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

This pattern is useful when you need to build a new list step by step.

---

## List Comprehensions

A list comprehension is a compact way to create a new list from an iterable.

Normal loop version:

```python
cubes = []

for number in range(1, 11):
    cubes.append(number ** 3)

print(cubes)
```

List comprehension version:

```python
cubes = [number ** 3 for number in range(1, 11)]

print(cubes)
```

Both create the same list:

```text
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

### When to Use a List Comprehension

Use a list comprehension when:

```text
- you are creating a new list
- the logic is simple
- the normal loop starts to feel repetitive
```

If the comprehension feels confusing, write the normal loop first.

---

## Slicing Lists

A slice lets you work with part of a list.

Example:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
```

### `players[0:3]`

```python
print(players[0:3])
```

Output:

```text
["charles", "martina", "michael"]
```

This returns items at indexes `0`, `1`, and `2`.

The stop index `3` is not included.

### `players[:3]`

```python
print(players[:3])
```

Output:

```text
["charles", "martina", "michael"]
```

This starts at the beginning and returns the first three items.

### `players[1:4]`

```python
print(players[1:4])
```

Output:

```text
["martina", "michael", "florence"]
```

This returns items at indexes `1`, `2`, and `3`.

### `players[-3:]`

```python
print(players[-3:])
```

Output:

```text
["michael", "florence", "eli"]
```

This returns the last three items in the list.

---

## Slicing Rule

Use this mental model:

```text
list[start:stop]
```

The slice includes `start`.

The slice stops before `stop`.

```text
start is included
stop is excluded
```

---

## Copying Lists

To copy a list correctly, use a full slice:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
```

This creates a separate list.

Example:

```python
my_foods.append("cannoli")
friend_foods.append("ice cream")

print(my_foods)
print(friend_foods)
```

Output:

```text
["pizza", "falafel", "carrot cake", "cannoli"]
["pizza", "falafel", "carrot cake", "ice cream"]
```

Each list can now change independently.

---

## Copying Mistake

This does not create a copy:

```python
friend_foods = my_foods
```

It makes both variables point to the same list.

Example:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods

my_foods.append("cannoli")
friend_foods.append("ice cream")

print(my_foods)
print(friend_foods)
```

Both lists show the same values, because both names refer to the same list.

### Rule

```text
new_list = old_list[:]  # creates a copy
new_list = old_list     # points to the same list
```

---

## Tuples

A tuple is an ordered collection of values that cannot be changed item by item.

Example:

```python
dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])
```

Tuples use parentheses:

```python
dimensions = (200, 50)
```

Lists use square brackets:

```python
dimensions = [200, 50]
```

---

## Tuples vs Lists

A list is mutable:

```python
foods = ["rice", "beans", "salad"]
foods[0] = "pasta"
```

A tuple is immutable:

```python
foods = ("rice", "beans", "salad")
foods[0] = "pasta"  # TypeError
```

You cannot modify one item inside a tuple.

But you can reassign the variable to a new tuple:

```python
foods = ("rice", "beans", "salad")
foods = ("pasta", "beans", "salad")
```

---

## When to Use Tuples

Use a tuple when the values should not change item by item.

Examples:

```python
dimensions = (200, 50)
coordinates = (10, 20)
rgb_color = (255, 255, 255)
```

---

## PEP 8 and Style

PEP 8 is Python's style guide.

Important beginner rules:

```text
- use 4 spaces for indentation
- use clear variable names
- keep lines readable
- do not use excessive blank lines
- make code easy to read
```

Code is read more often than it is written.

Clear code is easier to:

```text
- debug
- review
- refactor
- share with other developers
```

---

## Code Review Checklist

When reviewing Chapter 4 code, check:

```text
- Does the file run?
- Is indentation correct?
- Are variable names clear?
- Is the loop variable singular?
- Is the list variable plural?
- Is the final message outside the loop when needed?
- Did I use range() with the correct stop value?
- Did I use [:] when copying a list?
- Did I avoid excessive blank lines?
- Can I explain every line?
```

---

## Key Corrections from Self-Review

### Slices

Incorrect idea:

```text
players[0:3] returns the fourth item.
```

Correct idea:

```text
players[0:3] returns the first three items: indexes 0, 1, and 2.
```

### Copying Lists

Incorrect idea:

```text
friend_foods = my_foods creates a copy.
```

Correct idea:

```text
friend_foods = my_foods points to the same list.
friend_foods = my_foods[:] creates a copy.
```

### Tuples

Less precise:

```text
A tuple is a list that does not change.
```

More precise:

```text
A tuple is an ordered collection whose items cannot be changed item by item.
```

---

## Review Questions

Use these to check understanding.

1. What does a `for` loop do?
- A `for` loop repeats a block of code once for each item in a sequence.

2. What is the loop variable?
- The loop variable temporarily stores the current item during each pass through the loop.

3. How does indentation affect a loop?
- Indentation tells Python which lines belong inside the loop.
- Indented lines run once for each item.
- Unindented lines after the loop run once after the loop is finished.

4. What does `range(1, 5)` produce?
- It produces the numbers `1`, `2`, `3`, and `4`.
- The stop value `5` is not included.

5. Why does `range(1, 21)` print 1 through 20?
- `range()` excludes the stop value.
- To include `20`, the stop value must be `21`.

6. What does the third argument in `range(start, stop, step)` do?
- The third argument controls the step size.
- It tells Python how much to increase the number each time.

7. What does `players[0:3]` return?
- It returns a new list containing items at indexes `0`, `1`, and `2`.
- The stop index `3` is not included.

8. What does `players[-3:]` return?
- It returns the last three items in the list.

9. How do you copy a list correctly?
- Use a full slice: `new_list = old_list[:]`.
- This creates a separate list object.

10. What is the difference between a list and a tuple?
- A list is mutable, so its items can be changed.
- A tuple is immutable, so its items cannot be changed item by item.

11. Why should code be easy to read?
- Code is read more often than it is written.
- Clear code is easier to debug, review, refactor, test, and share with other developers.

12. What should you check during code review?
- Check that the file runs.
- Check indentation.
- Check clear variable names.
- Check that loop variables are singular and list variables are plural.
- Check that code is inside or outside the loop intentionally.
- Check that `range()` uses the correct stop value.
- Check that list copies use `[:]` when a separate copy is needed.
- Check that blank lines are not excessive.
- Check that you can explain every line.