# Chapter 1 Notes — Getting Started

These notes summarize the most important ideas from **Python Crash Course Chapter 1: Getting Started**.

---

## What Chapter 1 Is About

Chapter 1 introduces the basic workflow for writing and running Python programs.

The main goal is to get comfortable with:

```text
- writing a Python file
- running a Python file
- reading output
- fixing simple errors
- using the terminal
- using a code editor
```

---

## Python Files

Python programs are usually saved with the `.py` extension.

Example:

```text
hello_world.py
```

A Python file can contain one or more lines of Python code.

Example:

```python
print("Hello Python world!")
```

When the file runs, Python reads the code and executes it.

---

## `print()`

`print()` displays output in the terminal.

Example:

```python
print("Hello Python world!")
```

Output:

```text
Hello Python world!
```

Use `print()` when you want to see a value while learning or debugging.

Later, when writing functions, prefer `return` when the value needs to be reused or tested.

---

## Strings

A string is text inside quotes.

Examples:

```python
"Hello"
'Python'
"Hello Python world!"
```

Both single quotes and double quotes work.

Use one style consistently unless the string itself contains quotes.

Example:

```python
print("I'm learning Python.")
```

---

## Running a Python File

From the terminal, run a file with:

```bash
python3 hello_world.py
```

The command means:

```text
Use Python 3 to run the file named hello_world.py.
```

If the file is inside a folder, include the path:

```bash
python3 python/python-crash-course/chapter-01-getting-started-exercises/hello_world.py
```

---

## Errors

Errors are normal.

A traceback tells you:

```text
- what type of error happened
- where the error happened
- which line caused the problem
```

Example mistake:

```python
print("Hello Python world!
```

This causes a syntax error because the closing quote is missing.

Correct:

```python
print("Hello Python world!")
```

---

## Common Mistakes

### Missing quotes

Incorrect:

```python
print(Hello Python world!)
```

Correct:

```python
print("Hello Python world!")
```

### Missing parenthesis

Incorrect:

```python
print("Hello Python world!"
```

Correct:

```python
print("Hello Python world!")
```

### Running from the wrong folder

If Python says the file cannot be found, check:

```bash
pwd
ls
```

Then run the file with the correct path.

---

## Developer Habit

When something breaks, ask:

```text
1. What line caused the error?
2. What does the error message say?
3. Did I forget a quote, parenthesis, colon, or indentation?
4. Am I running the correct file?
5. Am I in the correct folder?
```

---

## Review Questions

1. What does a `.py` file contain?
- A `.py` file contains Python code.
- It can contain one line or many lines of instructions for Python to run.

2. What does `print()` do?
- `print()` displays output in the terminal.
- It is useful when you want to show a message, inspect a value, or debug while learning.

3. How do you run a Python file from the terminal?
- Use `python3` followed by the file path.
- If the file is inside a folder, include the full relative path.

4. What does a traceback help you find?
- A traceback helps you find:
  - what type of error happened
  - which file caused the error
  - which line caused the error
  - sometimes, what Python expected instead

5. Why should Python filenames use lowercase letters and underscores?
- Lowercase filenames with underscores are easier to read and follow common Python style.
- Avoid capital letters, spaces, and hyphens in Python filenames.

6. What should you check if Python says a file cannot be found?
- Check that you are in the correct folder.
- Check that the file name is spelled correctly.
- Check that the file path is correct.
- Use `pwd` to see your current folder.
- Use `ls` to list files in the current folder.

7. What is a string?
- A string is text inside quotes.
- Strings can use single quotes or double quotes.

8. Why are errors normal when learning programming?
- Errors are part of the programming process.
- They help you find what Python could not understand or run.
- Learning to read errors is a core developer skill, not a failure.
