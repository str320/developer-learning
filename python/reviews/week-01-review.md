# Week: 1 Review

## Week: 1 — Python Syntax, Variables, Functions

## Dates: April 24 – April 28

## Total hours studied: 20

## What I studied:
- Python Crash Course Chapter 1
- Python Crash Course Chapter 2
- Exercism Hello World
- Exercism Guido's Gorgeous Lasagna
- Exercism Currency Exchange
- Week 1 custom drills

## Exercises completed:
- Python Crash Course Chapter 1 selected exercises
- Python Crash Course Chapter 2 selected exercises
- Week 1 drills

## Exercism exercises completed:
- Exercism Hello World
- Exercism Lasagna
- Exercism Currency Exchange

## Book chapters/sections completed:
- Chapter 1: Python setup, running files, syntax basics
- Chapter 2: Variables, strings, numbers, comments, and constants

## What transferred easily from JavaScript:
- Variables transferred easily because the basic idea is the same: store a value with a name and use it later.

- Functions also transferred well. Python uses `def` instead of `function` or arrow functions, but the idea of parameters, arguments, and return values is familiar.

- String interpolation also made sense because Python f-strings are similar to JavaScript template literals.

- Arithmetic operations were straightforward because operators like `+`, `-`, `*`, and `/` work similarly.
What felt different in Python:
- Indentation feels more important in Python because it replaces JavaScript braces `{}`.

- Python functions use `def`, a colon, and indentation instead of curly braces.

- Constants are not enforced by the language. They are written in uppercase by convention, like `EXPECTED_BAKE_TIME`.

- Python string methods such as `.title()`, `.strip()`, `.removeprefix()`, and `.removesuffix()` return new strings instead of changing the original string directly.

- The difference between `print()` and `return` became clearer. Exercism tests expect returned values, not printed output.
Bugs I fixed:
- Fixed functions that needed to return values instead of only printing.
- Fixed small expected-output differences such as missing punctuation.
- Fixed string-method usage by remembering that methods like `.removeprefix()` return a new string.
- Fixed drill code so manual `print()` calls are protected by `if __name__ == "__main__":`.
- Fixed the Currency Exchange bill calculation to return an integer number of bills.
Code I refactored:
I refactored the Week 1 drills to separate reusable function definitions from manual test calls.

I also improved some functions by removing unnecessary conversions and reusing helper

### Before:
``` python
def elapsed_time_in_minutes(number_of_layers, minutes_in_oven):
return (number_of_layers * PREPARATION_TIME_PER_LAYER) + minutes_in_oven


def age_message(name, age):
return f"{name} is {str(age)} years old"
```

### After:
```python
def age_message(name, age):
return f"{name} is {age} years old."


def elapsed_time_in_minutes(number_of_layers, minutes_in_oven):
return preparation_time_in_minutes(number_of_layers) + minutes_in_oven
```

## Main thing I understand better now:
- I understand the difference between print() and return much better now.

- print() displays information in the terminal, but return sends a value back from a function so other code or tests can use it.

- I also understand why if __name__ == "__main__": is useful. It lets me run manual test code when I execute a file directly, but prevents that code from running when another file imports my functions.


## Main thing that still feels weak:
I still need more practice with writing clean Python style automatically.

I understand the concepts, but I want to get faster at:
- using correct indentation
- naming variables clearly
- knowing when to create constants
- organizing test calls
- writing simple assert tests
- avoiding unnecessary code like str() inside f-strings

## Questions for review:
- When should I use a constant instead of a normal variable?
    - Use a constant when the value should not change while the program runs.

- When should I write a helper function?
    - when I notice repeated logic, or when one part of the program has a clear smaller job.

- Is it better to use int(amount // denomination) or int(amount / denomination) in Currency Exchange?
    - because // clearly communicates that I want whole bills only.

- How many tests should I write for small practice functions?
    -  one normal case
    - one different normal case
    - one edge case if there is one

## Example:
```python
assert add_two(5) == 7
assert add_two(0) == 2
assert add_two(-2) == 0
```

- When should I use print() in real code
    - Use print() when I want to show information to the user or inspect something while debugging.

    - Use return when a function needs to give a value back to the rest of the program.

## Next week’s focus:
Week 2 will focus on:
- lists
- indexing
- modifying lists
- adding and removing items
- sorting
- loops
- range()
- slicing
- tuples
- Armstrong Numbers on Exercism

The main goal is to become comfortable working with collections of values and looping through them cleanly in Python.
