# Week 3 Drills — Booleans, Comparisons, Conditionals

These drills support **Week 3** of the Python study plan.

Focus topics:

- booleans
- truth value testing
- comparison operators
- `if`, `elif`, `else`
- `and`, `or`, `not`
- `in` and `not in`
- clean boolean-return functions
- avoiding unnecessary `if-else`
- writing small tests
- reading official documentation

Recommended folder:

```text
python/drills/week-03/
```

Recommended files:

```text
week_03_drills.py
week_03_drills_README.md
test_week_03_drills.py
docs_practice.py
```

---

# Suggested Test File

Put these tests in `test_week_03_drills.py`.

Recommended filename:

```text
test_week_03_drills.py
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
python3 python/drills/week-03/week_03_drills.py
```

Run the tests:

```bash
pytest python/drills/week-03/test_week_03_drills.py
```

---

# Documentation Practice File



```text
python/drills/week-03/docs_practice.py
```

Official docs sections to read:

- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Boolean Operations — `and`, `or`, `not`](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)

Use `docs_practice.py` for small experiments:

```python
print(bool([]))
print(bool([1, 2, 3]))
print(bool(""))
print(bool("python"))
print(bool(0))
print(bool(42))

print(True and False)
print(True or False)
print(not True)

print(5 > 3)
print(5 == 5)
print(5 != 3)
```

Record what you learned in:

```text
Obsidian: 01_notes/python_crash_course/chapter_05_notes.md
```

---

# Drill 1 — Is Even

## Task

Write a function called `is_even()`.

It should receive a number and return `True` if the number is even.

## Concepts

- modulo `%`
- equality comparison
- boolean return values

## Starter code

```python
number = 4
```

<details>
<summary>Show starter code</summary>

```python
def is_even(number):
    return number % 2 == 0
```

</details>

## Expected behavior

```python
is_even(4)  # True
is_even(5)  # False
```

---

# Drill 2 — Can Vote

## Task

Write a function called `can_vote()`.

It should receive an age and return `True` if the age is at least 18.

## Concepts

- numerical comparisons
- `>=`
- boolean return values

## Starter code

```python
age = 18
```

<details>
<summary>Show starter code</summary>

```python
def can_vote(age):
    return age >= 18
```

</details>

## Expected behavior

```python
can_vote(18)  # True
can_vote(17)  # False
```

---

# Drill 3 — Is Empty

## Task

Write a function called `is_empty()`.

It should receive a list and return `True` if the list is empty.

## Concepts

- `len()`
- equality comparison
- empty lists
- boolean return values

## Starter code

```python
items = []
```

<details>
<summary>Show starter code</summary>

```python
def is_empty(items):
    return len(items) == 0
```

</details>

## Expected behavior

```python
is_empty([])          # True
is_empty(["python"])  # False
```

---

# Drill 4 — Has Admin Access

## Task

Write a function called `has_admin_access()`.

It should receive a username and return `True` only if the username is `"admin"`.

## Concepts

- string comparison
- equality
- boolean return values

## Starter code

```python
username = "admin"
```

<details>
<summary>Show starter code</summary>

```python
def has_admin_access(username):
    return username == "admin"
```

</details>

## Expected behavior

```python
has_admin_access("admin")  # True
has_admin_access("strat")  # False
```

---

# Drill 5 — Is Valid Username

## Task

Write a function called `is_valid_username()`.

It should receive a username and return `True` if the username has at least 3 characters.

## Concepts

- `len()`
- `>=`
- validation
- boolean return values

## Starter code

```python
username = "ada"
```

<details>
<summary>Show starter code</summary>

```python
def is_valid_username(username):
    return len(username) >= 3
```

</details>

## Expected behavior

```python
is_valid_username("ada")  # True
is_valid_username("ab")   # False
```

---

# Drill 6 — Is Adult

## Task

Write a function called `is_adult()`.

It should receive an age and return `True` if the age is 18 or older.

## Concepts

- numerical comparisons
- duplicate practice
- clean boolean-return functions

## Starter code

```python
age = 21
```

<details>
<summary>Show starter code</summary>

```python
def is_adult(age):
    return age >= 18
```

</details>

## Expected behavior

```python
is_adult(21)  # True
is_adult(12)  # False
```

---

# Drill 7 — Is Positive

## Task

Write a function called `is_positive()`.

It should receive a number and return `True` if the number is greater than 0.

## Concepts

- numerical comparisons
- `>`
- boolean return values

## Starter code

```python
number = 5
```

<details>
<summary>Show starter code</summary>

```python
def is_positive(number):
    return number > 0
```

</details>

## Expected behavior

```python
is_positive(5)   # True
is_positive(0)   # False
is_positive(-3)  # False
```

---

# Drill 8 — Is Passing Grade

## Task

Write a function called `is_passing_grade()`.

It should receive a score and return `True` if the score is 60 or higher.

## Concepts

- numerical comparisons
- `>=`
- validation logic

## Starter code

```python
score = 75
```

<details>
<summary>Show starter code</summary>

```python
def is_passing_grade(score):
    return score >= 60
```

</details>

## Expected behavior

```python
is_passing_grade(90)  # True
is_passing_grade(60)  # True
is_passing_grade(59)  # False
```

---

# Drill 9 — Has Items

## Task

Write a function called `has_items()`.

It should receive a list and return `True` if the list has at least one item.

## Concepts

- truth value testing
- `bool()`
- empty lists
- non-empty lists

## Starter code

```python
items = ["python"]
```

<details>
<summary>Show starter code</summary>

```python
def has_items(items):
    return bool(items)
```

</details>

## Expected behavior

```python
has_items([])          # False
has_items(["python"])  # True
```

---

# Drill 10 — Can Enter Club

## Task

Write a function called `can_enter_club()`.

It should receive an age and a `has_id` boolean.

It should return `True` only if the person is at least 18 and has ID.

## Concepts

- `and`
- numerical comparisons
- combining conditions
- boolean parameters

## Starter code

```python
age = 20
has_id = True
```

<details>
<summary>Show starter code</summary>

```python
def can_enter_club(age, has_id):
    return age >= 18 and has_id
```

</details>

## Expected behavior

```python
can_enter_club(20, True)   # True
can_enter_club(20, False)  # False
can_enter_club(16, True)   # False
```

---

# Drill 11 — Is Discount Eligible

## Task

Write a function called `is_discount_eligible()`.

It should receive an age and return `True` if the person is younger than 18 or 65 or older.

## Concepts

- `or`
- comparison operators
- multiple valid conditions

## Starter code

```python
age = 16
```

<details>
<summary>Show starter code</summary>

```python
def is_discount_eligible(age):
    return age < 18 or age >= 65
```

</details>

## Expected behavior

```python
is_discount_eligible(16)  # True
is_discount_eligible(30)  # False
is_discount_eligible(70)  # True
```

---

# Drill 12 — Is Available Username

## Task

Write a function called `is_available_username()`.

It should receive a username and a list of current users.

It should return `True` if the username is not already taken.

The check should be case-insensitive.

## Concepts

- `not in`
- `.lower()`
- list comprehensions
- case-insensitive comparison

## Starter code

```python
username = "Ada"
current_users = ["admin", "ada", "eric"]
```

<details>
<summary>Show starter code</summary>

```python
def is_available_username(username, current_users):
    current_users_lower = [user.lower() for user in current_users]
    return username.lower() not in current_users_lower
```

</details>

## Expected behavior

```python
is_available_username("Ada", ["admin", "ada", "eric"])    # False
is_available_username("maria", ["admin", "ada", "eric"])  # True
```

---

# Challenge — User Status

## Task

Write a function called `user_status()`.

It should receive a username and return:

```text
"admin" if the username is "admin"
"guest" if the username is an empty string
"user" for any other username
```

## Concepts

- `if`
- `elif`
- `else`
- truth value testing
- ordered conditions

## Starter code

```python
username = "admin"
```

<details>
<summary>Show starter code</summary>

```python
def user_status(username):
    if username == "admin":
        return "admin"
    elif not username:
        return "guest"
    else:
        return "user"
```

</details>

## Expected behavior

```python
user_status("admin")  # "admin"
user_status("")       # "guest"
user_status("strat")  # "user"
```

---

# Suggested Test Section

Add this to the bottom of `week_03_drills.py`:

```python
if __name__ == "__main__":
    assert is_even(4) is True
    assert is_even(5) is False

    assert can_vote(18) is True
    assert can_vote(17) is False

    assert is_empty([]) is True
    assert is_empty(["python"]) is False

    assert has_admin_access("admin") is True
    assert has_admin_access("strat") is False

    assert is_valid_username("ada") is True
    assert is_valid_username("ab") is False

    assert is_adult(21) is True
    assert is_adult(12) is False

    assert is_positive(5) is True
    assert is_positive(0) is False
    assert is_positive(-3) is False

    assert is_passing_grade(90) is True
    assert is_passing_grade(60) is True
    assert is_passing_grade(59) is False

    assert has_items([]) is False
    assert has_items(["python"]) is True

    assert can_enter_club(20, True) is True
    assert can_enter_club(20, False) is False
    assert can_enter_club(16, True) is False

    assert is_discount_eligible(16) is True
    assert is_discount_eligible(30) is False
    assert is_discount_eligible(70) is True

    assert is_available_username("Ada", ["admin", "ada", "eric"]) is False
    assert is_available_username("maria", ["admin", "ada", "eric"]) is True

    assert user_status("admin") == "admin"
    assert user_status("") == "guest"
    assert user_status("strat") == "user"

    print("All Week 3 drill tests passed.")
```

---

# Suggested Pytest File

Put this in `test_week_03_drills.py`:

```python
from week_03_drills import (
    is_even,
    can_vote,
    is_empty,
    has_admin_access,
    is_valid_username,
    is_adult,
    is_positive,
    is_passing_grade,
    has_items,
    can_enter_club,
    is_discount_eligible,
    is_available_username,
    user_status,
)


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False


def test_can_vote():
    assert can_vote(18) is True
    assert can_vote(17) is False


def test_is_empty():
    assert is_empty([]) is True
    assert is_empty(["python"]) is False


def test_has_admin_access():
    assert has_admin_access("admin") is True
    assert has_admin_access("strat") is False


def test_is_valid_username():
    assert is_valid_username("ada") is True
    assert is_valid_username("ab") is False


def test_is_adult():
    assert is_adult(21) is True
    assert is_adult(12) is False


def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(0) is False
    assert is_positive(-3) is False


def test_is_passing_grade():
    assert is_passing_grade(90) is True
    assert is_passing_grade(60) is True
    assert is_passing_grade(59) is False


def test_has_items():
    assert has_items([]) is False
    assert has_items(["python"]) is True


def test_can_enter_club():
    assert can_enter_club(20, True) is True
    assert can_enter_club(20, False) is False
    assert can_enter_club(16, True) is False


def test_is_discount_eligible():
    assert is_discount_eligible(16) is True
    assert is_discount_eligible(30) is False
    assert is_discount_eligible(70) is True


def test_is_available_username():
    assert is_available_username("Ada", ["admin", "ada", "eric"]) is False
    assert is_available_username("maria", ["admin", "ada", "eric"]) is True


def test_user_status():
    assert user_status("admin") == "admin"
    assert user_status("") == "guest"
    assert user_status("strat") == "user"
```

---

# Quiz

1. What does `number % 2 == 0` check?
- It checks whether a number is even.

2. Why does `return age >= 18` work?
- Because `age >= 18` already evaluates to `True` or `False`.

3. What does `len(items) == 0` check?
- It checks whether a list is empty.

4. What does `bool([])` return?
- It returns `False`.

5. What does `bool(["python"])` return?
- It returns `True`.

6. What does `and` require to return `True`?
- Both sides must be truthy.

7. What does `or` require to return `True`?
- At least one side must be truthy.

8. What does `not` do?
- It reverses the truth value.

9. Why should boolean-return functions avoid unnecessary `if-else`?
- Because the comparison already returns a boolean result.

10. Why do we use `.lower()` for username checks?
- To make the comparison case-insensitive.

---

# Feedback Criteria

Your Week 3 drills are complete when:

- [ ] every function runs
- [ ] every function returns a value
- [ ] boolean-return functions return comparisons directly
- [ ] no logic function relies on unnecessary `print()`
- [ ] comparison operators are correct
- [ ] `and`, `or`, and `not` are used correctly
- [ ] `in` and `not in` are used correctly
- [ ] username checks are case-insensitive when needed
- [ ] truthy and falsy values are understood
- [ ] all `assert` tests pass
- [ ] all `pytest` tests pass
- [ ] you can explain each function line by line
- [ ] you made at least one cleanup/refactor pass

---

# Key Takeaways

- Comparisons return `True` or `False`.
- Boolean-return functions should be direct.
- `and` requires both sides to be truthy.
- `or` requires at least one side to be truthy.
- `not` reverses a truth value.
- Empty lists, empty strings, `0`, and `None` are falsy.
- Non-empty lists, non-empty strings, and non-zero numbers are usually truthy.
- Use `in` to check membership.
- Use `not in` to check absence.
- Use `.lower()` when capitalization should not matter.
- These drills prepare you for Exercism Bools, Comparisons, Conditionals, and Raindrops.
