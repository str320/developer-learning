# Week 4 Drills — Dictionaries and While Loops

These drills practice the main Week 4 skills from **Python Crash Course Chapter 6 and Chapter 7**.

The goal is to write small, runnable functions, test them, review them, and then refactor.

---

## Focus Topics

```text
- dictionaries
- key-value pairs
- accessing dictionary values
- .get()
- .items()
- .keys()
- .values()
- nested dictionaries
- while loops
- input()
- int()
- active flags
- break
- list processing with while
- pop()
- remove()
- append()
```

---

## Recommended Folder

```text
python/drills/week-04/
```

---

## Recommended Files

```text
python/drills/week-04/week_04_drills.py
python/drills/week-04/test_week_04_drills.py
python/drills/week-04/docs_practice.py
python/drills/week-04/week_04_drills_README.md
```

---

## How to Use These Drills

Use this order:

```text
1. Read the drill.
2. Write the simplest working version.
3. Run the function manually.
4. Add or run pytest tests.
5. Explain the function line by line.
6. Refactor only after it works.
```

Do not print inside the drill functions unless the drill specifically asks for printing.

Most functions should **return** values.

---

# Drill 1 — Build a User Profile Dictionary

Write a function named:

```python
build_user_profile(first_name, last_name, age, city)
```

The function should return a dictionary with these keys:

```text
first_name
last_name
age
city
```

## Concepts Practiced

```text
- creating dictionaries
- using parameters as values
- returning data
```

## Starter Code

```python
first_name = "ada"
last_name = "lovelace"
age = 36
city = "london"
```

<details>
<summary>Show starter code</summary>

```python
def build_user_profile(first_name, last_name, age, city):
    pass
```

</details>

## Expected Behavior

```python
build_user_profile("ada", "lovelace", 36, "london")
```

Expected result:

```python
{
    "first_name": "ada",
    "last_name": "lovelace",
    "age": 36,
    "city": "london",
}
```

## What to Notice

The dictionary keys are fixed names.  
The dictionary values come from the function parameters.

---

# Drill 2 — Get a City Safely with `.get()`

Write a function named:

```python
get_user_city(user)
```

The function receives a dictionary.

If the dictionary has a `city` key, return the city.

If the dictionary does not have a `city` key, return:

```text
Unknown city
```

## Concepts Practiced

```text
- reading dictionary values
- using .get()
- avoiding KeyError
- fallback values
```

## Starter Code

```python
user = {"name": "guido", "city": "haarlem"}
```

<details>
<summary>Show starter code</summary>

```python
def get_user_city(user):
    pass
```

</details>

## Expected Behavior

```python
get_user_city({"name": "guido", "city": "haarlem"})
# "haarlem"

get_user_city({"name": "ada"})
# "Unknown city"
```

## What to Notice

Square bracket access can crash if a key is missing.  
`.get()` can return a fallback value instead.

---

# Drill 3 — Count Favorite Languages

Write a function named:

```python
count_favorite_languages(favorite_languages)
```

The function receives a dictionary where:

```text
key = person's name
value = favorite programming language
```

Return a new dictionary that counts how many times each language appears.

## Concepts Practiced

```text
- looping through dictionary values
- .values()
- counting repeated values
- building a new dictionary
```

## Starter Code

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "python",
    "phil": "python",
    "erin": "java",
}
```

<details>
<summary>Show starter code</summary>

```python
def count_favorite_languages(favorite_languages):
    pass
```

</details>

## Expected Behavior

```python
count_favorite_languages({
    "jen": "python",
    "sarah": "c",
    "edward": "python",
})
```

Expected result:

```python
{
    "python": 2,
    "c": 1,
}
```

## What to Notice

Use `.values()` when you only need the values from a dictionary.

---

# Drill 4 — List Admin Users

Write a function named:

```python
list_admin_users(users)
```

The function receives a list of user dictionaries.

Each user dictionary has:

```text
username
role
```

Return a list containing only usernames where the role is:

```text
admin
```

## Concepts Practiced

```text
- list of dictionaries
- looping through records
- conditional checks
- appending selected values
```

## Starter Code

```python
users = [
    {"username": "admin_user", "role": "admin"},
    {"username": "regular_user", "role": "member"},
    {"username": "moderator_user", "role": "admin"},
]
```

<details>
<summary>Show starter code</summary>

```python
def list_admin_users(users):
    pass
```

</details>

## Expected Behavior

```python
list_admin_users([
    {"username": "admin_user", "role": "admin"},
    {"username": "regular_user", "role": "member"},
    {"username": "moderator_user", "role": "admin"},
])
```

Expected result:

```python
["admin_user", "moderator_user"]
```

## What to Notice

A list of dictionaries is common when each dictionary represents one record.

---

# Drill 5 — Move Pending Orders

Write a function named:

```python
move_pending_orders(pending_orders)
```

The function receives a list of pending sandwich orders.

Move every order into a new list called finished orders.

Return the finished orders list.

## Concepts Practiced

```text
- while loops
- list truthiness
- .pop()
- .append()
- moving items between lists
```

## Starter Code

```python
pending_orders = ["tuna", "veggie", "chicken"]
```

<details>
<summary>Show starter code</summary>

```python
def move_pending_orders(pending_orders):
    pass
```

</details>

## Expected Behavior

```python
move_pending_orders(["tuna", "veggie", "chicken"])
```

Expected result:

```python
["chicken", "veggie", "tuna"]
```

## What to Notice

`.pop()` removes the last item by default.  
That means the finished list may be in reverse order.

---

# Drill 6 — Remove an Unavailable Item

Write a function named:

```python
remove_unavailable_item(items, unavailable_item)
```

The function receives a list and an item that should be removed from the list.

Remove all copies of that item.

Return the cleaned list.

## Concepts Practiced

```text
- while loops
- membership checks with in
- .remove()
- repeated values
```

## Starter Code

```python
items = ["pastrami", "tuna", "pastrami", "veggie", "pastrami"]
unavailable_item = "pastrami"
```

<details>
<summary>Show starter code</summary>

```python
def remove_unavailable_item(items, unavailable_item):
    pass
```

</details>

## Expected Behavior

```python
remove_unavailable_item(
    ["pastrami", "tuna", "pastrami", "veggie", "pastrami"],
    "pastrami",
)
```

Expected result:

```python
["tuna", "veggie"]
```

## What to Notice

`.remove()` removes only the first matching value.  
To remove all copies, use a loop.

---

# Challenge — Summarize Poll Responses

Write a function named:

```python
summarize_poll_responses(responses)
```

The function receives a list of dictionaries.

Each dictionary has:

```text
name
language
```

Return a dictionary where:

```text
key = programming language
value = number of people who chose that language
```

## Concepts Practiced

```text
- list of dictionaries
- reading dictionary values
- counting
- .get()
- building a summary dictionary
```

## Starter Code

```python
responses = [
    {"name": "ada", "language": "python"},
    {"name": "guido", "language": "python"},
    {"name": "linus", "language": "c"},
]
```

<details>
<summary>Show starter code</summary>

```python
def summarize_poll_responses(responses):
    pass
```

</details>

## Expected Behavior

```python
summarize_poll_responses([
    {"name": "ada", "language": "python"},
    {"name": "guido", "language": "python"},
    {"name": "linus", "language": "c"},
])
```

Expected result:

```python
{
    "python": 2,
    "c": 1,
}
```

---

# Suggested Test File

Create this file:

```text
python/drills/week-04/test_week_04_drills.py
```

## Starter Code

```python
from week_04_drills import build_user_profile
```

<details>
<summary>Show starter code</summary>

```python
from week_04_drills import (
    build_user_profile,
    get_user_city,
    count_favorite_languages,
    list_admin_users,
    move_pending_orders,
    remove_unavailable_item,
    summarize_poll_responses,
)
```

</details>

Add tests gradually after each drill works.

Suggested first test:

```python
def test_build_user_profile():
    assert build_user_profile("ada", "lovelace", 36, "london") == {
        "first_name": "ada",
        "last_name": "lovelace",
        "age": 36,
        "city": "london",
    }
```

Run tests from the Week 4 drill folder:

```bash
cd python/drills/week-04
pytest
```

---

# Suggested `docs_practice.py`

Use this file only for tiny runnable documentation experiments.

## Starter Code

```python
print(bool([]))
print(bool(["order"]))
```

<details>
<summary>Show starter code</summary>

```python
print(bool([]))
print(bool(["order"]))

print({"city": "london"}.get("city"))
print({}.get("city", "Unknown city"))

orders = ["tuna", "veggie"]
while orders:
    print(orders.pop())
```

</details>

---

# Quiz

1. What is a dictionary?
- A dictionary is a Python collection that stores information as named pairs. It is useful when one object has several related pieces of information.

2. What is a key-value pair?
- A key-value pair is one item inside a dictionary. The key is the name or label, and the value is the data connected to that key.
3. What does `.get()` help you avoid?
- `.get()` helps avoid a `KeyError` when a key is missing from a dictionary.
4. What is the difference between `user["city"]` and `user.get("city")`?
- `user["city"]` expects the key to exist and raises an error if it does not. `user.get("city")` safely checks for the key and returns `None` or a fallback value if the key is missing.
5. When should you use `.values()`?
- Use `.values()` when you only need the values from a dictionary and do not need the keys.
6. When should you use `.items()`?
- Use `.items()` when you need both the key and the value while looping through a dictionary.
7. Why does `while pending_orders:` stop when the list becomes empty?
- A non-empty list is truthy, and an empty list is falsy. When the list becomes empty, the loop condition becomes false and the loop stops.
8. Why must you check for `"quit"` before calling `int()`?
- You must check for `"quit"` first because `"quit"` is text and cannot be converted into an integer. If Python tries to convert it, the program raises a `ValueError`.
9. What does `.pop()` do?
- .pop()` removes an item from a list and returns the removed item. By default, it removes the last item in the list.
10. What does `.remove()` do when there are repeated values?
-  `.remove()` removes only the first matching value. If the same value appears multiple times, a loop is needed to remove all copies.
11. Why should these drill functions return values instead of printing?
-  Functions should return values because returned values are easier to test, reuse, compare, and combine with other code. Printing is mainly for showing output to the user.
12. What is the difference between a flag and `break`?
- A flag is a variable that controls whether a loop should continue running. `break` exits the loop immediately. A flag changes the loop condition; `break` stops the loop directly.

---

# Feedback Criteria

Your Week 4 drills are complete when:

```text
- every function runs
- every function returns a value
- no logic function relies on unnecessary print()
- dictionary keys are named clearly
- missing keys are handled safely when required
- while loops stop correctly
- repeated values are handled correctly
- all manual checks pass
- all pytest tests pass
- you can explain each function line by line
- you made one cleanup/refactor pass after the code worked
```

Review in this order:

```text
1. Correctness
2. Edge cases
3. Readability
4. Naming
5. Return vs print
6. Helper logic
7. Tests
8. Style
```

---

# Key Takeaways

```text
- Use dictionaries when one object needs named pieces of information.
- Use .get() when a key might be missing.
- Use .values() when you only need values.
- Use .items() when you need both keys and values.
- Use a list of dictionaries when you have many similar records.
- Use while loops when repetition depends on changing state.
- Check for quit before converting input with int().
- Return values from functions so they are easier to test.
```

---

# Completion Checklist

- [ x ] Create `week_04_drills.py`
- [ x ] Create `test_week_04_drills.py`
- [ x ] Create `docs_practice.py`
- [ x ] Complete Drill 1
- [ x ] Complete Drill 2
- [ x ] Complete Drill 3
- [ x ] Complete Drill 4
- [ x ] Complete Drill 5
- [ x ] Complete Drill 6
- [ x ] Complete the challenge
- [ x ] Run manual tests
- [ x ] Add pytest tests
- [ x ] Run pytest
- [ x ] Refactor after tests pass
- [ x ] Commit the finished files

---

# Git Workflow

From the repo root:

```bash
git status
git add python/drills/week-04
git commit -m "Add Week 4 dictionary and while loop drills"
git pull --rebase origin main
git push
```
