# Week 1 Python Drills

## Focus

Week 1 focuses on the basics you need before starting the first 
Exercism exercises:
- running Python files
- `print()` vs `return`
- variables
- constants
- strings and f-strings
- numbers
- arithmetic
- type conversion
- indentation
- simple functions

Recommended file for your answers:

```text
python/drills/week_01_drills.py
```

Run the file from the project root:

```bash
python3 python/drills/week_01_drills.py
```

---

# Drill 1 — `print()` vs `return`

Write these functions:

```python
def show_greeting(name):
    # prints: Hello, Ada!
    pass


def make_greeting(name):
    # returns: Hello, Ada!
    pass
```

Expected behavior:

```python
show_greeting("Ada")
# prints Hello, Ada!

message = make_greeting("Ada")
print(message)
# prints Hello, Ada!
```

Focus:

- `print()` displays a value.
- `return` gives a value back to the caller.

---

# Drill 2 — Simple Arithmetic Functions

Write:

```python
def add_two(number):
    pass


def double(number):
    pass


def square(number):
    pass
```

Expected:

```python
add_two(5)     # 7
double(6)      # 12
square(4)      # 16
```

Focus:

- parameters
- return values
- arithmetic expressions

---

# Drill 3 — Constants

Create a constant:

```python
MINUTES_IN_HOUR = 60
```

Then write:

```python
def hours_to_minutes(hours):
    pass
```

Expected:

```python
hours_to_minutes(2)   # 120
hours_to_minutes(5)   # 300
```

Focus:

- constants are written in uppercase by convention
- constants make repeated values easier to understand and update

---

# Drill 4 — Lasagna-Style Practice

Create these constants:

```python
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2
```

Write:

```python
def bake_time_remaining(minutes_in_oven):
    pass


def preparation_time_in_minutes(number_of_layers):
    pass


def elapsed_time_in_minutes(number_of_layers, minutes_in_oven):
    pass
```

Expected:

```python
bake_time_remaining(30)              # 10
preparation_time_in_minutes(3)       # 6
elapsed_time_in_minutes(3, 20)       # 26
```

Focus:

- constants
- function parameters
- arithmetic
- return values

This prepares you directly for Exercism: Guido’s Gorgeous Lasagna.

---

# Drill 5 — Strings and f-strings

Write:

```python
def introduce(name, language):
    pass
```

Expected:

```python
introduce("Strat", "Python")
# "Hi, I am Strat and I am learning Python."
```

Use an f-string.

Focus:

- Python f-strings are similar to JavaScript template literals.

---

# Drill 6 — Type Conversion

Write:

```python
def age_message(name, age):
    pass
```

Expected:

```python
age_message("Ada", 36)
# "Ada is 36 years old."
```

Use an f-string.

Then write:

```python
def add_string_numbers(first, second):
    pass
```

Expected:

```python
add_string_numbers("10", "5")   # 15
```

Focus:

- converting strings to integers with `int()`
- combining values safely in strings

---

# Drill 7 — Currency-Style Practice

Write:

```python
def exchange_money(budget, exchange_rate):
    pass


def get_change(budget, exchanging_value):
    pass
```

Expected:

```python
exchange_money(100, 1.25)      # 80.0
get_change(100, 40)            # 60
```

Focus:

- division
- subtraction
- clear function names
- return values

This prepares you for Exercism: Currency Exchange.

---

# Drill 8 — Debugging Syntax Mistakes

Create this broken code and fix it:

```python
def favorite_language(name, language)
    return f"{name} likes {language}"
```

Questions:

1. What error do you get?
- You get a `SyntaxError`.

2. Which line is wrong?
- The function definition line is wrong:

```python
def favorite_language(name, language)
```

3. What character is missing?
- The colon `:` is missing at the end of the function definition.

4. Why does Python care about it?
- Python uses the colon to mark the start of an indented code block. Without the colon, Python does not know that the next indented lines belong to the function.

Corrected code:

```python
def favorite_language(name, language):
    return f"{name} likes {language}"
```

Focus:

- reading tracebacks
- identifying syntax errors
- noticing missing punctuation

---

# Drill 9 — Indentation Practice

Fix this:

```python
def multiply_by_three(number):
return number * 3
```

Expected:

```python
multiply_by_three(4)   # 12
```

Focus:

- Python indentation replaces JavaScript braces.

---

# Drill 10 — Mini Review Function Set

Write all of these in one file:

```python
def minutes_to_seconds(minutes):
    pass


def days_to_hours(days):
    pass


def total_study_minutes(hours, minutes):
    pass


def completed_lesson_message(lesson_name):
    pass
```

Expected:

```python
minutes_to_seconds(3)               # 180
days_to_hours(2)                    # 48
total_study_minutes(2, 30)          # 150
completed_lesson_message("Ch. 1")   # "Completed: Ch. 1"
```

Focus:

- combining Week 1 skills
- clear function names
- returning values
- simple arithmetic
- f-strings

---

# Manual Test Calls

At the bottom of `week_01_drills.py`, add temporary test calls:

```python
print(add_two(5))
print(hours_to_minutes(2))
print(bake_time_remaining(30))
print(introduce("Strat", "Python"))
```

Run:

```bash
python3 python/drills/week_01_drills.py
```

When the output is correct, commit:

```bash
git add .
git commit -m "Add week 1 Python drills"
git push
```

---

# Week 1 Quiz

Answer these in your own words.

## Question 1

What is the difference between `print()` and `return`?

- `print()` displays a value in the terminal.
- `return` sends a value back from a function to the caller.
- Use `print()` when you want the user to see output.
- Use `return` when you want to reuse, store, or test a value.

Example:

```python
def show_greeting(name):
    print(f"Hello, {name}!")


def make_greeting(name):
    return f"Hello, {name}!"
```

## Question 2

Why is `EXPECTED_BAKE_TIME` written in uppercase?

- It is written in uppercase because it is a constant.
- A constant is a value that should not change during the program.
- Python does not force constants to stay unchanged, but uppercase names tell other developers: “Do not change this value.”

Example:

```python
EXPECTED_BAKE_TIME = 40
```

## Question 3

What does this return?

```python
int("5")
```

- It returns the integer `5`.

Explanation:

```python
int("5")  # 5
```

The original value is a string. `int()` converts it into an integer.

## Question 4

Why does this code fail?

```python
def add(a, b)
    return a + b
```

- It fails because the function definition is missing a colon `:` at the end of the `def` line.

Correct version:

```python
def add(a, b):
    return a + b
```

## Question 5

Why does this code fail?

```python
def add(a, b):
return a + b
```

- It fails because `return a + b` is not indented.
- In Python, indentation defines the function body.
- The `return` line must be inside the function.

Correct version:

```python
def add(a, b):
    return a + b
```

## Question 6

What does this function return?

```python
def double(number):
    return number * 2

double(6)
```

- It returns `12`.

Explanation:

```python
6 * 2 == 12
```

## Question 7

What is the Python equivalent of a JavaScript template literal?

- The Python equivalent is an f-string.

JavaScript:

```javascript
`Hello, ${name}!`
```

Python:

```python
f"Hello, {name}!"
```

## Question 8

What is the difference between a parameter and an argument?

Example:

```python
def greet(name):
    return f"Hello, {name}!"

greet("Ada")
```

- `name` is the parameter.
- `"Ada"` is the argument.
- A parameter is the variable name in the function definition.
- An argument is the real value passed into the function call.

---

# Stretch Challenge

Create a second file:

```text
python/drills/week_01_extra_challenge.py
```

Write:

```python
def weekly_study_summary(hours_studied, target_hours):
    pass
```

Expected:

```python
weekly_study_summary(12, 20)
# "You studied 12 hours. You have 8 hours left this week."
```

Then add:

```python
def study_session_minutes(hours, minutes):
    pass
```

Expected:

```python
study_session_minutes(1, 45)
# 105
```

---

# Feedback Criteria

Before sending your solution for review, check:

- Did each function return the correct value?
- Did you avoid unnecessary `print()` inside logic functions?
- Are your variable names clear?
- Are constants written in uppercase?
- Is your indentation correct?
- Is your arithmetic correct?
- Can you explain every line?
- Did you test normal examples?
- Did you test at least one different value?
- Is the code readable?

---

# Suggested Commit Messages

```bash
git commit -m "Add week 1 drills README"
git commit -m "Complete print vs return drills"
git commit -m "Complete Week 1 arithmetic drills"
git commit -m "Complete lasagna-style drills"
git commit -m "Complete Week 1 quiz"
```

---

# What to Study Next

After completing these drills:

1. Start Python Crash Course Chapter 1.
2. Create and run `hello_world.py`.
3. Complete Exercism: Hello World.
4. Complete Exercism: Guido’s Gorgeous Lasagna.
5. Send one solution for review.
6. Refactor after feedback.

# Extra Review Quiz

1. Why does `f"{age}"` not need `str(age)`?
- Inside an f-string, Python automatically converts the value to text for display.

2. Why is it better to reuse `preparation_time_in_minutes()`?
- Reusing the helper function avoids repeated logic.
- This follows the DRY principle: Don’t Repeat Yourself.
- If the preparation rule changes later, you only need to update one function.

3. What does `if __name__ == "__main__":` protect you from?
- It prevents temporary test code or print calls from running automatically when the file is imported into another file or test file.

4. Why does Python need a colon after `def favorite_language(name, language):`?
- Python uses the colon to mark the start of an indented code block.
- The indented block becomes the function body.
