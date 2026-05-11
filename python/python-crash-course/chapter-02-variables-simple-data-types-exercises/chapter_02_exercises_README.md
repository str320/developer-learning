# Python Crash Course — Chapter 2 Exercises

## Chapter 2 — Variables and Simple Data Types

This folder contains practice exercises for **Python Crash Course Chapter 2: Variables and Simple Data Types**.

The goal of this chapter is to learn how to:

- assign values to variables
- change variable values
- use strings
- use string methods like `title()`, `upper()`, and `lower()`
- use f-strings
- strip whitespace with `lstrip()`, `rstrip()`, and `strip()`
- remove suffixes with `removesuffix()`
- work with numbers
- use comments
- write small programs in separate files

Recommended folder:

```text
python/python-crash-course/chapter-02-variables-simple-data-types/
```

Recommended file names:

```text
exercise_2_1_simple_message.py
exercise_2_2_simple_messages.py
exercise_2_3_personal_message.py
exercise_2_4_name_cases.py
exercise_2_5_famous_quote.py
exercise_2_6_famous_quote_2.py
exercise_2_7_stripping_names.py
exercise_2_8_file_extensions.py
exercise_2_9_number_eight.py
exercise_2_10_favorite_number.py
exercise_2_11_adding_comments.py
```

---

# Exercise 2-1 — Simple Message

## Task

Assign a message to a variable, and then print that message.

## Concepts

- variables
- strings
- `print()`

## Starter code

```python
message = "I am learning Python."
```

<details>
<summary>Show starter code</summary>

```python
print(message)
```

</details>

## Goal

Practice storing a string in a variable and printing it.

---

# Exercise 2-2 — Simple Messages

## Task

Assign a message to a variable and print that message.

Then change the value of the variable to a new message and print the new message.

## Concepts

- variable assignment
- variable reassignment
- strings
- `print()`

## Starter code

```python
message = "I am learning Python."
```

<details>
<summary>Show starter code</summary>

```python
print(message)

message = "I am learning variables and strings."
print(message)
```

</details>

## Goal

Understand that a variable can be reassigned to a new value.

---

# Exercise 2-3 — Personal Message

## Task

Use a variable to represent a person’s name.

Print a message to that person.

Example:

```text
Hello Eric, would you like to learn some Python today?
```

## Concepts

- variables
- f-strings
- personalized messages

## Starter code

```python
name = "Eric"
```

<details>
<summary>Show starter code</summary>

```python
print(f"Hello {name}, would you like to learn some Python today?")
```

</details>

## Goal

Practice using a variable inside a string with an f-string.

---

# Exercise 2-4 — Name Cases

## Task

Use a variable to represent a person’s name.

Print that person’s name in:

1. lowercase
2. uppercase
3. title case

## Concepts

- string methods
- `lower()`
- `upper()`
- `title()`

## Starter code

```python
name = "Eric"
```

<details>
<summary>Show starter code</summary>

```python
print(name.lower())
print(name.upper())
print(name.title())
```

</details>

## Goal

Practice using common string case methods.

---

# Exercise 2-5 — Famous Quote

## Task

Find a quote from a famous person you admire.

Print the quote and the name of its author.

Your output should look similar to:

```text
Albert Einstein once said, "A person who never made a mistake never tried anything new."
```

## Concepts

- strings
- quotes inside strings
- f-strings or direct printing

## Starter code

```python
quote = "A person who never made a mistake never tried anything new."
```

<details>
<summary>Show starter code</summary>

```python
print(f'Albert Einstein once said, "{quote}"')
```

</details>

## Goal

Practice working with quotation marks inside strings.

---

# Exercise 2-6 — Famous Quote 2

## Task

Repeat Exercise 2-5, but this time:

1. Store the famous person’s name in a variable called `famous_person`.
2. Compose the message and store it in a variable called `message`.
3. Print the message.

## Concepts

- variables
- f-strings
- composing a message
- storing final output in a variable

## Starter code

```python
famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
```

<details>
<summary>Show starter code</summary>

```python
message = f'{famous_person} once said, "{quote}"'
print(message)
```

</details>

## Goal

Practice building a complete message from smaller variables.

---

# Exercise 2-7 — Stripping Names

## Task

Use a variable to represent a person’s name.

Include whitespace characters at the beginning and end of the name.

Make sure you use each character combination at least once:

- `\t`
- `\n`

Print the name once so the whitespace is visible.

Then print the name using each stripping function:

- `lstrip()`
- `rstrip()`
- `strip()`

## Concepts

- whitespace
- tabs
- newlines
- `lstrip()`
- `rstrip()`
- `strip()`

## Starter code

```python
name = "\tEric\n"
```

<details>
<summary>Show starter code</summary>

```python
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
```

</details>

## Goal

Understand how Python removes whitespace from the left side, right side, or both sides of a string.

---

# Exercise 2-8 — File Extensions

## Task

Python has a `removesuffix()` method that works like `removeprefix()`.

Assign the value `"python_notes.txt"` to a variable called `filename`.

Use `removesuffix()` to display the filename without the file extension.

## Concepts

- string methods
- `removesuffix()`
- returned values
- original string vs new string

## Starter code

```python
filename = "python_notes.txt"
```

<details>
<summary>Show starter code</summary>

```python
print(filename.removesuffix(".txt"))
```

</details>

## Important Note

String methods like `removesuffix()` return a new string.

They do not modify the original variable unless you reassign the result:

```python
filename = filename.removesuffix(".txt")
print(filename)
```

## Goal

Practice removing a suffix from a string.

---

# Exercise 2-9 — Number Eight

## Task

Write addition, subtraction, multiplication, and division operations that each result in the number `8`.

Each operation should be inside a `print()` call.

Your output should be four lines, with the number `8` appearing once on each line.

## Concepts

- addition
- subtraction
- multiplication
- division
- `print()`

## Starter code

```python
# Write four print() calls.
```

<details>
<summary>Show starter code</summary>

```python
print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 / 2)
```

</details>

## Note

In Python, division with `/` returns a float.

So:

```python
print(16 / 2)
```

prints:

```text
8.0
```

That is acceptable while learning division.

## Goal

Practice basic arithmetic operators.

---

# Exercise 2-10 — Favorite Number

## Task

Use a variable to represent your favorite number.

Then use that variable to create a message that reveals your favorite number.

Print that message.

## Concepts

- variables
- numbers
- f-strings
- converting values inside strings

## Starter code

```python
favorite_number = 8
```

<details>
<summary>Show starter code</summary>

```python
message = f"My favorite number is {favorite_number}."
print(message)
```

</details>

## Goal

Practice putting a number inside an f-string.

---

# Exercise 2-11 — Adding Comments

## Task

Choose two programs you have written.

Add at least one comment to each.

If you do not have anything specific to write because the programs are simple, add:

1. your name
2. the current date
3. one sentence describing what the program does

## Concepts

- comments
- code explanation
- readability

## Starter code

```python
# Strat
# May 24
# This program prints a simple message.
```

<details>
<summary>Show starter code</summary>

```python
message = "I am learning Python."
print(message)
```

</details>

## Goal

Practice writing useful comments without over-commenting simple code.

---

# Suggested Workflow

For each exercise:

1. Create a separate file.
2. Write the code from memory.
3. Run the file.
4. Fix any errors.
5. Add a short comment if useful.
6. Commit after a meaningful group of exercises.

Example:

```bash
python3 python/python-crash-course/chapter-02-variables-simple-data-types/simple_message.py
```

Commit examples:

```bash
git add .
git commit -m "Complete Chapter 2 variable exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 2 string exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 2 number exercises"
git push
```

---

# Chapter 2 Completion Checklist

Mark each exercise when completed.

- [x] 2-1 Simple Message
- [x] 2-2 Simple Messages
- [x] 2-3 Personal Message
- [x] 2-4 Name Cases
- [x] 2-5 Famous Quote
- [x] 2-6 Famous Quote 2
- [x] 2-7 Stripping Names
- [x] 2-8 File Extensions
- [x] 2-9 Number Eight
- [x] 2-10 Favorite Number
- [x] 2-11 Adding Comments

---

# Self-Review Questions

Answer these after finishing the chapter.

## Variables

1. What is a variable?
- A variable is a name that refers to a value in a program.
2. What happens when I assign a new value to an existing variable?
- The variable name now refers to the new value.
3. Why should variable names be clear?
- Clear variable names make the purpose of the value easier to understand.

## Strings

4. What is a string?
- A string is a sequence of characters, usually text.
5. What does `title()` do?
- `title()` returns a new string with the first letter of each word capitalized.
6. What does `upper()` do?
- `upper()` returns a new string with all letters uppercase.
7. What does `lower()` do?
- `lower()` returns a new string with all letters lowercase.
8. What is an f-string?
- An f-string is a string that lets you insert variable values or expressions inside `{}`.

## Whitespace

9. What does `lstrip()` remove?
- `lstrip()` removes whitespace from the left side of a string.
10. What does `rstrip()` remove?
- `rstrip()` removes whitespace from the right side of a string.
11. What does `strip()` remove?- `strip()` removes whitespace from both the left and right sides of a string.

## String Suffixes

12. What does `removesuffix(".txt")` return?
- It returns a new string with `".txt"` removed from the end, if the string ends with `".txt"`.

13. Does `removesuffix()` change the original variable automatically?
- No. Strings are immutable, so `removesuffix()` returns a new string. To keep the result, assign it to a variable.


## Numbers

14. What is the difference between `8` and `8.0`?
- `8` is an integer. `8.0` is a float.
15. Why does `16 / 2` return `8.0`?
 In Python, `/` always returns a float, even when the result is a whole number.

## Developer Habits

16. Did I run every file?
17. Did I use lowercase filenames with underscores?
18. Did I commit my completed work?
19. Can I explain every line I wrote?

---

# Common Mistakes to Watch For

## Forgetting to print a variable

```python
message = "Hello"
```

This stores the message, but does not display it.

Use:

```python
print(message)
```

---

## Forgetting that string methods return new strings

```python
filename = "python_notes.txt"
filename.removesuffix(".txt")
print(filename)
```

This still prints:

```text
python_notes.txt
```

Use:

```python
filename = filename.removesuffix(".txt")
print(filename)
```

or:

```python
print(filename.removesuffix(".txt"))
```

---

## Missing f before an f-string

Incorrect:

```python
name = "Eric"
print("Hello {name}")
```

Output:

```text
Hello {name}
```

Correct:

```python
name = "Eric"
print(f"Hello {name}")
```

Output:

```text
Hello Eric
```

---

# Key Takeaways

- Variables store values.
- Variables can be reassigned.
- Strings are text values.
- F-strings let you insert variables into strings.
- String methods like `title()`, `upper()`, and `lower()` return new strings.
- `strip()` methods remove whitespace.
- `removesuffix()` returns a new string without the suffix.
- Arithmetic operators work similarly to JavaScript.
- `/` division returns a float.
- Comments explain code when the code alone is not enough.
