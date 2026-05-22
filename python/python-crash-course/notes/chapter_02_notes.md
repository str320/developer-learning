# Chapter 2 Notes — Variables and Simple Data Types

These notes summarize the most important ideas from **Python Crash Course Chapter 2: Variables and Simple Data Types**.

---

## What Chapter 2 Is About

Chapter 2 introduces the basic building blocks of Python programs:

```text
- variables
- strings
- string methods
- f-strings
- numbers
- constants
- comments
```

---

## Variables

A variable stores a value so it can be used later.

Example:

```python
message = "Hello Python world!"
print(message)
```

The variable name is:

```python
message
```

The value is:

```python
"Hello Python world!"
```

You can change the value of a variable:

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

The second assignment replaces the first value.

---

## Naming Variables

Good variable names are clear and readable.

Good:

```python
first_name = "ada"
favorite_number = 7
```

Avoid unclear names:

```python
x = "ada"
n = 7
```

Short names are sometimes acceptable in small examples, but clear names are better while learning.

---

## Strings

A string is text inside quotes.

Examples:

```python
name = "ada lovelace"
message = 'Hello Python!'
```

Strings can use single or double quotes.

Use double quotes when the string contains an apostrophe:

```python
message = "I'm learning Python."
```

---

## String Methods

A method is an action attached to an object.

Example:

```python
name = "ada lovelace"

print(name.title())
print(name.upper())
print(name.lower())
```

Output:

```text
Ada Lovelace
ADA LOVELACE
ada lovelace
```

### Important Rule

String methods return a new string.

They do not permanently change the original string unless you assign the result back.

Example:

```python
name = "ada"
name.title()

print(name)  # ada
```

To save the changed version:

```python
name = "ada"
name = name.title()

print(name)  # Ada
```

---

## f-strings

An f-string lets you insert variables into a string.

Example:

```python
first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"

print(full_name)
```

Output:

```text
ada lovelace
```

You can also call methods inside an f-string:

```python
print(f"Hello, {full_name.title()}!")
```

---

## Whitespace

Whitespace means spaces, tabs, and newlines.

Examples:

```python
print("Python")
print("\tPython")
print("Languages:\nPython\nJavaScript")
```

Useful escape characters:

```text
\t = tab
\n = newline
```

---

## Stripping Whitespace

These methods remove extra whitespace:

```python
name = "  ada  "

print(name.lstrip())
print(name.rstrip())
print(name.strip())
```

What they do:

```text
lstrip() removes whitespace from the left
rstrip() removes whitespace from the right
strip() removes whitespace from both sides
```

Like other string methods, they return a new string.

To save the cleaned version:

```python
name = "  ada  "
name = name.strip()
```

---

## Removing Prefixes and Suffixes

Python has string methods for removing text from the beginning or end.

Example:

```python
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
```

Output:

```text
python_notes
```

Important: this returns a new string.

---

## Numbers

Python can work with integers and floats.

Integers:

```python
age = 25
```

Floats:

```python
price = 19.99
```

Basic operations:

```python
print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 / 2)
```

Exponentiation:

```python
print(2 ** 3)  # 8
```

---

## Underscores in Numbers

You can use underscores to make large numbers easier to read.

```python
universe_age = 14_000_000_000
print(universe_age)
```

Python ignores the underscores when running the code.

---

## Multiple Assignment

You can assign multiple variables in one line:

```python
x, y, z = 0, 1, 2
```

This means:

```python
x = 0
y = 1
z = 2
```

---

## Constants

A constant is a value that should not change.

Python does not enforce constants, but the convention is to write them in uppercase.

Example:

```python
MAX_CONNECTIONS = 5000
EXPECTED_BAKE_TIME = 40
```

Use a constant when the value represents a fixed rule or configuration.

---

## Comments

Comments explain code for humans.

Example:

```python
# Say hello to the user.
print("Hello!")
```

Use comments to explain why the code exists, not every obvious line.

---

## Common Mistakes

### Using a variable before assigning it

Incorrect:

```python
print(message)
message = "Hello!"
```

Correct:

```python
message = "Hello!"
print(message)
```

### Forgetting that methods return new values

Incorrect if you expect `name` to change:

```python
name = "ada"
name.title()
print(name)  # ada
```

Correct:

```python
name = "ada"
name = name.title()
print(name)  # Ada
```

### Confusing `print()` and `return`

Use `print()` to display output.

Use `return` inside functions when the caller needs the value.

---

## Key Corrections from Chapter 2

### Constants vs variables

Use a constant when the value should stay fixed:

```python
EXPECTED_BAKE_TIME = 40
```

Use a normal variable when the value may change:

```python
elapsed_time = 30
```

### Helper functions

Write a helper function when the same logic may be reused.

Example:

```python
def bake_time_remaining(elapsed_time):
    return EXPECTED_BAKE_TIME - elapsed_time
```

---

## Review Questions

1. What is a variable?
- A variable is a name that refers to a value in a program.
- It lets you store a value so you can use it later.

2. Why should variable names be clear?
- Clear variable names make code easier to read, debug, and explain.
- A good name describes what the value represents.

3. What is a string?
- A string is text inside quotes.
- Strings can use single quotes or double quotes.

4. What does `.title()` do?
- `.title()` returns a new string with the first letter of each word capitalized.

5. Do string methods mutate the original string?
- No. String methods return a new string.
- They do not change the original string unless you assign the result back to a variable.

6. What is an f-string?
- An f-string lets you insert variables or expressions inside a string.
- It starts with `f` before the opening quote.

7. What does `\n` do?
- `\n` creates a newline inside a string.

8. What does `strip()` do?
- `.strip()` removes whitespace from both the left and right sides of a string.
- It returns a new cleaned string.
- Related methods: `lstrip()` removes whitespace from the left, and `rstrip()` removes whitespace from the right.

9. What is the difference between an integer and a float?
- An integer is a whole number.
- A float is a decimal number.

10. What does `**` mean?
- `**` means exponentiation.
- It raises a number to a power.

11. What is a constant?
- A constant is a value that should not change during the program.
- Python does not enforce constants, but the convention is to write them in uppercase.

12. When should I use a comment?
- Use a comment when it helps explain why the code exists or clarifies something that is not obvious.
- Avoid comments that only repeat what the code already clearly says.

13. What is the difference between `print()` and `return`?
- `print()` displays a value in the terminal.
- `return` sends a value back from a function so it can be reused, stored, or tested.
