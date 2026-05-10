# Chapter 5 Notes — If Statements

These notes summarize the most important ideas from **Python Crash Course Chapter 5: If Statements**.

---

## What Chapter 5 Is About

Chapter 5 introduces decision-making in Python.

You learned how to:

```text
- write conditional tests
- understand booleans
- compare values
- use if statements
- use if-else chains
- use if-elif-else chains
- use and / or / not
- check values in lists
- check whether a list is empty
- combine loops with conditionals
```

---

## Booleans

A boolean is a value that is either:

```python
True
False
```

Booleans usually answer yes/no questions.

Examples:

```python
age = 18

print(age >= 18)  # True
print(age < 18)   # False
```

---

## Conditional Tests

A conditional test is an expression that evaluates to `True` or `False`.

Example:

```python
car = "subaru"

print(car == "subaru")  # True
print(car == "audi")    # False
```

---

## Assignment vs Equality

Use `=` to assign a value.

```python
car = "subaru"
```

Use `==` to compare values.

```python
car == "subaru"
```

Common mistake:

```python
if car = "subaru":
    print("This is a Subaru.")
```

Correct:

```python
if car == "subaru":
    print("This is a Subaru.")
```

---

## Inequality

Use `!=` to check if two values are not equal.

Example:

```python
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")
```

---

## Numerical Comparisons

Common comparison operators:

```text
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to
```

Examples:

```python
age = 21

print(age == 21)
print(age != 18)
print(age > 18)
print(age < 65)
print(age >= 21)
print(age <= 30)
```

---

## `and`

`and` returns `True` only when both conditions are true.

Example:

```python
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)  # False
```

Both sides must be true.

---

## `or`

`or` returns `True` when at least one condition is true.

Example:

```python
age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)  # True
```

Only one side needs to be true.

---

## `not`

`not` reverses a boolean value.

Example:

```python
is_active = True

print(not is_active)  # False
```

Use `not` when you want the opposite of a condition.

---

## Checking Whether a Value Is in a List

Use `in` to check whether an item exists in a list.

Example:

```python
requested_toppings = ["mushrooms", "onions", "pineapple"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
```

---

## Checking Whether a Value Is Not in a List

Use `not in` to check whether an item is missing from a list.

Example:

```python
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response.")
```

---

## Simple `if` Statements

An `if` statement runs code only when a condition is true.

Example:

```python
age = 19

if age >= 18:
    print("You are old enough to vote!")
```

If the condition is false, the indented block is skipped.

---

## `if-else` Statements

Use `if-else` when there are two possible paths.

Example:

```python
age = 17

if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
```

---

## `if-elif-else` Chains

Use `if-elif-else` when there are more than two possible outcomes.

Example:

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
```

Python checks the conditions in order and runs the first true block.

---

## Why Order Matters

In an `if-elif-else` chain, Python stops after the first true condition.

Example:

```python
age = 12

if age < 18:
    print("Child or teenager")
elif age < 4:
    print("Toddler")
```

The second condition will never run for age `3`, because `age < 18` is already true.

Put more specific checks before broader checks.

---

## Independent `if` Statements

Use independent `if` statements when more than one condition can be true.

Example:

```python
favorite_fruits = ["banana", "apple", "mango"]

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "apple" in favorite_fruits:
    print("You really like apples!")
```

Both conditions can run.

Do not use `elif` if you want multiple matches.

---

## Checking If a List Is Empty

An empty list evaluates to `False`.

A non-empty list evaluates to `True`.

Example:

```python
requested_toppings = []

if requested_toppings:
    print("Adding toppings.")
else:
    print("Are you sure you want a plain pizza?")
```

This is called truth value testing.

---

## Using Multiple Lists

You can check requested values against available values.

Example:

```python
available_toppings = ["mushrooms", "olives", "pepperoni", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we do not have {topping}.")
```

This combines:

```text
- loops
- lists
- in
- if-else
```

---

## Case-Insensitive Checks

Use `.lower()` when capitalization should not matter.

Example:

```python
current_users = ["admin", "jaden", "ada", "eric", "guido"]
new_users = ["sarah", "ERIC", "maria", "Admin", "linus"]

current_users_lower = [user.lower() for user in current_users]

for username in new_users:
    if username.lower() in current_users_lower:
        print(f"{username} is already taken.")
    else:
        print(f"{username} is available.")
```

This prevents `"Admin"` and `"admin"` from being treated as different usernames.

---

## Common Mistakes

### Using JavaScript operators

Incorrect:

```python
if age >= 18 && age < 65:
    print("Adult")
```

Correct:

```python
if age >= 18 and age < 65:
    print("Adult")
```

Incorrect:

```python
if age < 18 || age >= 65:
    print("Discount")
```

Correct:

```python
if age < 18 or age >= 65:
    print("Discount")
```

### Lowercase booleans

Incorrect:

```python
is_active = true
```

Correct:

```python
is_active = True
```

### Checking multiple values incorrectly

Incorrect:

```python
if "banana" and "apple" in favorite_fruits:
    print("You like both.")
```

Correct:

```python
if "banana" in favorite_fruits and "apple" in favorite_fruits:
    print("You like both.")
```

### Forgetting `else`

If only one of two messages should print, use `else`.

Incorrect:

```python
if username in current_users:
    print("Username taken.")

print("Username available.")
```

Correct:

```python
if username in current_users:
    print("Username taken.")
else:
    print("Username available.")
```

---

## Official Docs Practice

Chapter 5 connects to these Python documentation topics:

```text
Truth Value Testing
Boolean Operations
Comparisons
```

### Official Reading Links

Read only these sections from the Python official documentation:

- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Boolean Operations — `and`, `or`, `not`](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)

Reference page:

- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)

When reading documentation, ask:

```text
1. What problem does this feature solve?
2. What syntax does it use?
3. What does it return?
4. What values are considered true or false?
5. Can I run one tiny example?
6. What mistake should I avoid?
```

### Small Experiments

```python
print(bool([]))          # False
print(bool([1, 2, 3]))   # True
print(bool(""))          # False
print(bool("python"))    # True
print(bool(0))           # False
print(bool(42))          # True

print(True and False)    # False
print(True or False)     # True
print(not True)          # False

print(5 > 3)             # True
print(5 == 5)            # True
print(5 != 3)            # True
```

---

## Key Corrections from Chapter 5

### Use `else` when only one result should print

In username checking, this is wrong:

```python
if username in current_users:
    print("Username taken.")

print("Username available.")
```

The availability message prints every time.

Use:

```python
if username in current_users:
    print("Username taken.")
else:
    print("Username available.")
```

### Normalize case before comparing usernames

Use:

```python
username.lower()
```

and compare against a lowercase copy of current users.

### Independent `if` statements are different from `elif`

Use independent `if` statements when more than one condition can be true.

Use `elif` when only one branch should run.

---

## Code Review Checklist

When reviewing Chapter 5 code, check:

```text
- Did I use == for comparison?
- Did I use = only for assignment?
- Did I avoid JavaScript operators like && and ||?
- Did I use True and False with capital letters?
- Is indentation correct?
- Are if / elif / else branches ordered correctly?
- Should these be independent if statements instead of elif?
- Should this second print be inside an else block?
- Did I normalize case with .lower() when needed?
- Can I explain why each condition is True or False?
```

---

## Review Questions

1. What is a boolean?
2. What is the difference between `=` and `==`?
3. What does `!=` mean?
4. What does `and` require to return `True`?
5. What does `or` require to return `True`?
6. What does `not` do?
7. What does `item in items` check?
8. What does `item not in items` check?
9. Why does `if requested_toppings:` work?
10. What does an empty list evaluate to?
11. When should I use independent `if` statements?
12. When should I use `if-elif-else`?
13. Why does order matter in an `if-elif-else` chain?
14. Why use `.lower()` for username checks?
15. Which JavaScript habits should I avoid in Python conditionals?
