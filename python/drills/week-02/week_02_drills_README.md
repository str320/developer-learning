# Week 2 Drills — Lists, Loops, Slicing, Tuples

These drills support **Week 2** of the Python study plan.

Focus topics:

- lists
- indexes
- negative indexes
- `for` loops
- `range()`
- `min()`, `max()`, `sum()`
- list comprehensions
- slicing
- copying lists
- tuples
- clean return values

Recommended folder:

```text
python/drills/week-02/
```

Recommended files:

```text
week_02_drills.py
week_02_drills_README.md
test_week_02_drills.py
```

---

# Suggested Test File
Put these tests in test_week_02_drills.py

Recommended filename:

```text
test_week_02_drills.py
```

---

# How to Use These Drills

For each drill:

1. Read the task.
2. Try to solve it without opening the hidden starter code.
3. Run the file.
4. Add simple `assert` tests.
5. Refactor after it works.
6. Make sure each function uses `return`, not unnecessary `print()`.

Run the file:

```bash
python3 python/drills/week-02/week_02_drills.py
```

---

# Drill 1 — First Item

## Task

Write a function called `first_item()`.

It should receive a list and return the first item.

## Concepts

- lists
- index `0`
- return values

## Starter code

```python
items = ["python", "django", "react"]
```

<details>
<summary>Show starter code</summary>

```python
def first_item(items):
    return items[0]
```

</details>

## Expected behavior

```python
first_item(["python", "django", "react"])  # "python"
```

---

# Drill 2 — Last Item

## Task

Write a function called `last_item()`.

It should receive a list and return the last item.

## Concepts

- lists
- negative indexes
- return values

## Starter code

```python
items = ["python", "django", "react"]
```

<details>
<summary>Show starter code</summary>

```python
def last_item(items):
    return items[-1]
```

</details>

## Expected behavior

```python
last_item(["python", "django", "react"])  # "react"
```

---

# Drill 3 — Total Numbers

## Task

Write a function called `total_numbers()`.

It should receive a list of numbers and return the total.

## Concepts

- lists of numbers
- `sum()`
- return values

## Starter code

```python
numbers = [1, 2, 3, 4, 5]
```

<details>
<summary>Show starter code</summary>

```python
def total_numbers(numbers):
    return sum(numbers)
```

</details>

## Expected behavior

```python
total_numbers([1, 2, 3, 4, 5])  # 15
```

---

# Drill 4 — Biggest Number

## Task

Write a function called `biggest_number()`.

It should receive a list of numbers and return the largest number.

## Concepts

- lists of numbers
- `max()`
- return values

## Starter code

```python
numbers = [3, 9, 2, 12, 5]
```

<details>
<summary>Show starter code</summary>

```python
def biggest_number(numbers):
    return max(numbers)
```

</details>

## Expected behavior

```python
biggest_number([3, 9, 2, 12, 5])  # 12
```

---

# Drill 5 — Smallest Number

## Task

Write a function called `smallest_number()`.

It should receive a list of numbers and return the smallest number.

## Concepts

- lists of numbers
- `min()`
- return values

## Starter code

```python
numbers = [3, 9, 2, 12, 5]
```

<details>
<summary>Show starter code</summary>

```python
def smallest_number(numbers):
    return min(numbers)
```

</details>

## Expected behavior

```python
smallest_number([3, 9, 2, 12, 5])  # 2
```

---

# Drill 6 — Double Numbers

## Task

Write a function called `double_numbers()`.

It should receive a list of numbers and return a new list where every number is doubled.

## Concepts

- `for` loops
- `append()`
- creating a new list
- return values

## Starter code

```python
numbers = [1, 2, 3, 4]
```

<details>
<summary>Show starter code</summary>

```python
def double_numbers(numbers):
    doubled = []

    for number in numbers:
        doubled.append(number * 2)

    return doubled
```

</details>

## Expected behavior

```python
double_numbers([1, 2, 3, 4])  # [2, 4, 6, 8]
```

---

# Drill 7 — Square Numbers

## Task

Write a function called `square_numbers()`.

It should receive a list of numbers and return a new list where every number is squared.

## Concepts

- `for` loops
- exponentiation with `**`
- `append()`
- creating a new list

## Starter code

```python
numbers = [1, 2, 3, 4]
```

<details>
<summary>Show starter code</summary>

```python
def square_numbers(numbers):
    squares = []

    for number in numbers:
        squares.append(number ** 2)

    return squares
```

</details>

## Expected behavior

```python
square_numbers([1, 2, 3, 4])  # [1, 4, 9, 16]
```

---

# Drill 8 — Long Words

## Task

Write a function called `long_words()`.

It should receive a list of words and return a new list containing only words longer than 5 characters.

## Concepts

- `for` loops
- `if` statements
- `len()`
- filtering lists

## Starter code

```python
words = ["python", "js", "django", "react", "postgres"]
```

<details>
<summary>Show starter code</summary>

```python
def long_words(words):
    result = []

    for word in words:
        if len(word) > 5:
            result.append(word)

    return result
```

</details>

## Expected behavior

```python
long_words(["python", "js", "django", "react", "postgres"])
# ["python", "django", "postgres"]
```

---

# Drill 9 — First Three Items

## Task

Write a function called `first_three()`.

It should receive a list and return the first three items.

## Concepts

- slicing
- start index
- stop index

## Starter code

```python
items = ["a", "b", "c", "d", "e"]
```

<details>
<summary>Show starter code</summary>

```python
def first_three(items):
    return items[:3]
```

</details>

## Expected behavior

```python
first_three(["a", "b", "c", "d", "e"])  # ["a", "b", "c"]
```

---

# Drill 10 — Last Three Items

## Task

Write a function called `last_three()`.

It should receive a list and return the last three items.

## Concepts

- slicing
- negative indexes

## Starter code

```python
items = ["a", "b", "c", "d", "e"]
```

<details>
<summary>Show starter code</summary>

```python
def last_three(items):
    return items[-3:]
```

</details>

## Expected behavior

```python
last_three(["a", "b", "c", "d", "e"])  # ["c", "d", "e"]
```

---

# Drill 11 — Copy and Add

## Task

Write a function called `copy_and_add()`.

It should receive a list and a new item.

It should return a copied list with the new item added.

The original list should not change.

## Concepts

- copying lists
- slicing with `[:]`
- `append()`
- mutation

## Starter code

```python
foods = ["pizza", "falafel", "carrot cake"]
```

<details>
<summary>Show starter code</summary>

```python
def copy_and_add(items, new_item):
    copied_items = items[:]
    copied_items.append(new_item)

    return copied_items
```

</details>

## Expected behavior

```python
foods = ["pizza", "falafel", "carrot cake"]

copy_and_add(foods, "cannoli")
# ["pizza", "falafel", "carrot cake", "cannoli"]

foods
# ["pizza", "falafel", "carrot cake"]
```

---

# Drill 12 — Tuple Menu

## Task

Write a function called `menu_items()`.

It should receive a tuple of foods and return a list containing each food title-cased.

## Concepts

- tuples
- `for` loops
- `.title()`
- creating a list from another iterable

## Starter code

```python
foods = ("rice", "beans", "salad")
```

<details>
<summary>Show starter code</summary>

```python
def menu_items(foods):
    formatted_foods = []

    for food in foods:
        formatted_foods.append(food.title())

    return formatted_foods
```

</details>

## Expected behavior

```python
menu_items(("rice", "beans", "salad"))
# ["Rice", "Beans", "Salad"]
```

---

# Challenge — Armstrong Helper

## Task

Write a function called `digit_powers()`.

It should receive a number and return a list of each digit raised to the power of the number of digits.

This prepares you for Exercism Armstrong Numbers.

## Concepts

- `str()`
- `int()`
- `len()`
- `for` loops
- exponentiation
- list building

## Starter code

```python
number = 153
```

<details>
<summary>Show starter code</summary>

```python
def digit_powers(number):
    digits = str(number)
    power = len(digits)
    powers = []

    for digit in digits:
        powers.append(int(digit) ** power)

    return powers
```

</details>

## Expected behavior

```python
digit_powers(153)  # [1, 125, 27]
digit_powers(9)    # [9]
digit_powers(9474) # [6561, 256, 2401, 256]
```

---

# Suggested Test Section

Add this to the bottom of `week_02_drills.py`:

```python
if __name__ == "__main__":
    assert first_item(["python", "django", "react"]) == "python"
    assert last_item(["python", "django", "react"]) == "react"
    assert total_numbers([1, 2, 3, 4, 5]) == 15
    assert biggest_number([3, 9, 2, 12, 5]) == 12
    assert smallest_number([3, 9, 2, 12, 5]) == 2
    assert double_numbers([1, 2, 3, 4]) == [2, 4, 6, 8]
    assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert long_words(["python", "js", "django", "react", "postgres"]) == [
        "python",
        "django",
        "postgres",
    ]
    assert first_three(["a", "b", "c", "d", "e"]) == ["a", "b", "c"]
    assert last_three(["a", "b", "c", "d", "e"]) == ["c", "d", "e"]

    foods = ["pizza", "falafel", "carrot cake"]
    copied_foods = copy_and_add(foods, "cannoli")

    assert copied_foods == ["pizza", "falafel", "carrot cake", "cannoli"]
    assert foods == ["pizza", "falafel", "carrot cake"]

    assert menu_items(("rice", "beans", "salad")) == ["Rice", "Beans", "Salad"]
    assert digit_powers(153) == [1, 125, 27]

    print("All Week 2 drill tests passed.")
```

---

# Quiz

1. What does `items[0]` return?
- Returns the first item in the list with index 0.
2. What does `items[-1]` return?
- Returns the last item in the list.
3. What does `items[:3]` return?
- Returns the first three items in the list with index from 0 to 2.
4. What does `items[-3:]` return?
- Returns the last three items in the list.
5. What is the difference between `items[:]` and `items`?
- `items[:]` creates a shallow copy of the list. `items` refers to the original list. They may contain the same values, but they are different list objects.
6. What does `sum(numbers)` return?
- It returns the total of all numbers.
7. Does `.append()` return a new list?
- No. `.append()` mutates the original list and returns `None`.

8. Why should most drill functions use `return` instead of `print()`?
- Because `return` gives the result back to the caller, so the value can be tested, reused, or stored.

9. What does `str(153)` return?
- A string with the numbers.
10. What does `int("5")` return?
- A number integer.

---

# Feedback Criteria

Your Week 2 drills are complete when:

- [x] every function runs
- [x] every function returns a value
- [x] no logic function relies on unnecessary `print()`
- [x] list-copying drills do not mutate the original list
- [x] loop variables are singular and readable
- [x] list variables are plural and readable
- [x] slicing answers are correct
- [x] all `assert` tests pass
- [x] you can explain each function line by line
- [x] you made at least one cleanup/refactor pass

---

# Key Takeaways

- Lists store multiple values.
- Loops process each item one at a time.
- `range()` helps generate number sequences.
- Slices return part of a list.
- `[:]` creates a list copy.
- Tuples are ordered collections that cannot be changed item by item.
- List comprehensions are useful after you understand the normal loop version.
- Armstrong Numbers combine strings, numbers, loops, `len()`, `int()`, and `sum()`.
