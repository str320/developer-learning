# Python Crash Course — Chapter 5 Exercises

## Chapter 5 — If Statements

This folder contains practice exercises for **Python Crash Course Chapter 5: If Statements**.

The goal of this chapter is to learn how to:

- write conditional tests
- understand `True` and `False`
- compare values with `==`, `!=`, `<`, `>`, `<=`, and `>=`
- use `if` statements
- use `if-else` chains
- use `if-elif-else` chains
- use `and`, `or`, and `not`
- check whether a value is in a list
- check whether a value is not in a list
- check whether a list is empty
- combine loops with conditional logic
- write cleaner conditional tests
- start reading official Python documentation

Recommended folder:

```text
python/python-crash-course/chapter-05-if-statements-exercises
```

Recommended files:

```text
README.md
chapter_05_notes.md
exercise_5_1_conditional_tests.py
exercise_5_2_more_conditional_tests.py
exercise_5_3_alien_colors_1.py
exercise_5_4_alien_colors_2.py
exercise_5_5_alien_colors_3.py
exercise_5_6_stages_of_life.py
exercise_5_7_favorite_fruit.py
exercise_5_8_hello_admin.py
exercise_5_9_no_users.py
exercise_5_10_checking_usernames.py
exercise_5_11_ordinal_numbers.py
exercise_5_12_styling_if_statements.md
exercise_5_13_your_ideas.md
```

---

# Chapter Notes

Create a chapter notes file:

```text
notes.md
```

Suggested sections:

```markdown
# Chapter 5 Notes — If Statements

## Booleans

## Conditional Tests

## Equality and Inequality

## Numerical Comparisons

## and / or / not

## Checking Values in Lists

## Checking If a List Is Empty

## if Statements

## if-else Chains

## if-elif-else Chains

## Official Docs Practice

### Truth Value Testing

### Boolean Operations

### Comparisons

### Small Experiments
```

---

# Example — Conditional Test

## Task

Create a variable and test whether it equals a specific value.

## Concepts

- equality
- boolean result
- `True`
- `False`

## Starter code

```python
car = "subaru"
```

<details>
<summary>Show starter code</summary>

```python
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")
```

</details>

## Goal

Understand that comparison expressions return either `True` or `False`.

---

# Example — if Statement

## Task

Use an `if` statement to run code only when a condition is true.

## Concepts

- `if`
- comparison
- indentation

## Starter code

```python
age = 19
```

<details>
<summary>Show starter code</summary>

```python
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

</details>

## Goal

Understand that indented code under an `if` statement runs only when the condition is true.

---

# Example — if-else Statement

## Task

Use `if-else` to choose between two possible paths.

## Concepts

- `if`
- `else`
- branching logic

## Starter code

```python
age = 17
```

<details>
<summary>Show starter code</summary>

```python
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
```

</details>

## Goal

Understand how Python chooses one block when the condition is true and another block when it is false.

---

# Example — if-elif-else Chain

## Task

Use an `if-elif-else` chain to assign a price based on age.

## Concepts

- `if`
- `elif`
- `else`
- ordered conditions

## Starter code

```python
age = 12
```

<details>
<summary>Show starter code</summary>

```python
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
```

</details>

## Goal

Understand how Python checks conditions in order and runs the first matching block.

---

# Exercise 5-1 — Conditional Tests

## Task

Write a series of conditional tests.

Print a statement describing each test and your prediction for the result.

Create at least:

- 10 tests total
- 5 tests that evaluate to `True`
- 5 tests that evaluate to `False`

## Concepts

- equality
- inequality
- boolean expressions
- predictions

## Starter code

```python
car = "subaru"
```

<details>
<summary>Show starter code</summary>

```python
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")
```

</details>

## Goal

Practice predicting whether conditional tests evaluate to `True` or `False`.

---

# Exercise 5-2 — More Conditional Tests

## Task

Write more conditional tests.

Include at least one `True` and one `False` result for each type:

1. Equality and inequality with strings
2. Tests using `.lower()`
3. Numerical tests
4. Tests using `and`
5. Tests using `or`
6. Test whether an item is in a list
7. Test whether an item is not in a list

## Concepts

- strings
- `.lower()`
- numbers
- comparison operators
- `and`
- `or`
- `in`
- `not in`

## Starter code

```python
language = "Python"
age = 21
favorite_languages = ["python", "javascript", "sql"]
```

<details>
<summary>Show starter code</summary>

```python
print("Is language == 'Python'? I predict True.")
print(language == "Python")

print("\nIs language == 'python'? I predict False.")
print(language == "python")

print("\nIs language.lower() == 'python'? I predict True.")
print(language.lower() == "python")

print("\nIs age >= 18 and age < 65? I predict True.")
print(age >= 18 and age < 65)

print("\nIs 'python' in favorite_languages? I predict True.")
print("python" in favorite_languages)

print("\nIs 'ruby' not in favorite_languages? I predict True.")
print("ruby" not in favorite_languages)
```

</details>

## Goal

Practice the most common types of conditional tests.

---

# Exercise 5-3 — Alien Colors #1

## Task

Imagine an alien was just shot down in a game.

Create a variable called `alien_color` and assign it one of these values:

```python
"green"
"yellow"
"red"
```

Then:

1. Write an `if` statement to test whether the alien is green.
2. If it is green, print a message that the player earned 5 points.
3. Write one version that passes the test.
4. Write one version that fails the test and has no output.

## Concepts

- `if`
- equality
- conditional output

## Starter code

```python
alien_color = "green"
```

<details>
<summary>Show starter code</summary>

```python
if alien_color == "green":
    print("You just earned 5 points!")
```

</details>

## Goal

Understand that an `if` block runs only when its condition is true.

---

# Exercise 5-4 — Alien Colors #2

## Task

Use an `if-else` chain.

Then:

1. If the alien is green, print that the player earned 5 points.
2. If the alien is not green, print that the player earned 10 points.
3. Write one version that runs the `if` block.
4. Write one version that runs the `else` block.

## Concepts

- `if`
- `else`
- equality
- branching

## Starter code

```python
alien_color = "green"
```

<details>
<summary>Show starter code</summary>

```python
if alien_color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
```

</details>

## Goal

Practice choosing between two possible outcomes.

---

# Exercise 5-5 — Alien Colors #3

## Task

Turn your `if-else` chain into an `if-elif-else` chain.

Rules:

- Green alien: 5 points
- Yellow alien: 10 points
- Red alien: 15 points

Write three versions of the program, making sure each message is printed for the correct alien color.

## Concepts

- `if`
- `elif`
- `else`
- multiple branches

## Starter code

```python
alien_color = "green"
```

<details>
<summary>Show starter code</summary>

```python
if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
else:
    print("You earned 15 points.")
```

</details>

## Goal

Practice handling more than two possible outcomes.

---

# Exercise 5-6 — Stages of Life

## Task

Write an `if-elif-else` chain that determines a person's stage of life.

Rules:

- Less than 2: baby
- At least 2 but less than 4: toddler
- At least 4 but less than 13: kid
- At least 13 but less than 20: teenager
- At least 20 but less than 65: adult
- 65 or older: elder

## Concepts

- numerical comparisons
- ordered conditions
- `if-elif-else`

## Starter code

```python
age = 25
```

<details>
<summary>Show starter code</summary>

```python
if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a kid.")
elif age < 20:
    print("This person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")
```

</details>

## Goal

Understand that ordered comparisons can cover ranges of values.

---

# Exercise 5-7 — Favorite Fruit

## Task

Make a list of your three favorite fruits called `favorite_fruits`.

Write five independent `if` statements.

Each `if` statement should check whether a fruit is in your list.

If the fruit is in your list, print a message such as:

```text
You really like bananas!
```

## Concepts

- lists
- `in`
- independent `if` statements

## Starter code

```python
favorite_fruits = ["banana", "apple", "mango"]
```

<details>
<summary>Show starter code</summary>

```python
if "banana" in favorite_fruits:
    print("You really like bananas!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "orange" in favorite_fruits:
    print("You really like oranges!")

if "kiwi" in favorite_fruits:
    print("You really like kiwis!")
```

</details>

## Goal

Understand that independent `if` statements are all checked separately.

---

# Exercise 5-8 — Hello Admin

## Task

Make a list of five or more usernames, including `"admin"`.

Loop through the list and print a greeting to each user.

Rules:

- If the username is `"admin"`, print a special greeting.
- Otherwise, print a generic greeting.

## Concepts

- lists
- `for` loops
- `if-else` inside a loop

## Starter code

```python
usernames = ["admin", "jaden", "ada", "eric", "guido"]
```

<details>
<summary>Show starter code</summary>

```python
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
```

</details>

## Goal

Practice combining loops from Chapter 4 with conditionals from Chapter 5.

---

# Exercise 5-9 — No Users

## Task

Add an `if` test to `hello_admin.py` to make sure the list of users is not empty.

Rules:

1. If the list is empty, print:
   ```text
   We need to find some users!
   ```
2. Remove all usernames from your list.
3. Make sure the correct message is printed.

## Concepts

- truth value testing
- empty lists
- `if`
- `else`

## Starter code

```python
usernames = []
```

<details>
<summary>Show starter code</summary>

```python
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
```

</details>

## Goal

Understand that an empty list is treated as false in an `if` statement.

---

# Exercise 5-10 — Checking Usernames

## Task

Simulate how websites make sure every username is unique.

Steps:

1. Make a list of five or more usernames called `current_users`.
2. Make another list of five usernames called `new_users`.
3. Make sure one or two new usernames are already in `current_users`.
4. Loop through `new_users`.
5. If the username already exists, print that the person needs to enter a new username.
6. If the username is available, print that the username is available.
7. Make the comparison case insensitive.

## Concepts

- lists
- loops
- `in`
- `.lower()`
- case-insensitive comparison
- list comprehensions

## Starter code

```python
current_users = ["admin", "jaden", "ada", "eric", "guido"]
new_users = ["sarah", "ERIC", "maria", "Admin", "linus"]
```

<details>
<summary>Show starter code</summary>

```python
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is already taken. Please enter a new username.")
    else:
        print(f"{new_user} is available.")
```

</details>

## Goal

Practice comparing user input safely by normalizing values with `.lower()`.

---

# Exercise 5-11 — Ordinal Numbers

## Task

Ordinal numbers indicate position in a list, such as `1st` or `2nd`.

Rules:

1. Store the numbers `1` through `9` in a list.
2. Loop through the list.
3. Use an `if-elif-else` chain inside the loop.
4. Print the proper ordinal ending for each number.

Expected output:

```text
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
```

## Concepts

- lists
- `for` loops
- `if-elif-else`
- f-strings

## Starter code

```python
numbers = list(range(1, 10))
```

<details>
<summary>Show starter code</summary>

```python
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
```

</details>

## Goal

Practice using an `if-elif-else` chain inside a loop.

---

# Exercise 5-12 — Styling if Statements

## Task

Review the programs you wrote in this chapter.

Make sure your conditional tests are styled appropriately.

Check:

1. Spaces around comparison operators
2. Clear variable names
3. Consistent indentation
4. No unnecessary blank lines
5. Readable output messages

## Concepts

- PEP 8
- code review
- readable conditionals

## Starter code

```text
Choose three Chapter 5 files to review.
```

<details>
<summary>Show starter code</summary>

```text
Recommended files:
- exercise_5_1_conditional_tests.py
- exercise_5_6_stages_of_life.py
- exercise_5_10_checking_usernames.py
```

</details>

## Goal

Practice reviewing and improving code after it already works.

---

# Exercise 5-13 — Your Ideas

## Task

Record new ideas for programs you might want to write as your skills improve.

Think about:

- games
- datasets
- web applications
- tools
- automations
- study projects

## Concepts

- project thinking
- problem solving
- planning

## Starter code

```text
Write your ideas in Markdown.
```

<details>
<summary>Show starter code</summary>

```markdown
# Exercise 5-13 — Your Ideas

## Games

## Data Projects

## Web Applications

## Tools and Automations

## Study Projects
```

</details>

## Goal

Start thinking like a developer by identifying problems you might solve with code.

---

# Official Docs Practice

Chapter 5 introduces booleans and conditionals, so this is the first week where official documentation practice becomes part of the plan.

Read selectively. Do not try to understand the entire documentation page at once.

## Docs sections to inspect

```text
Truth Value Testing
Boolean Operations
Comparisons
```

Use this checklist:

```text
1. What problem does this feature solve?
2. What syntax does it use?
3. What does it return?
4. What values are considered true or false?
5. Can I run one tiny example?
6. What mistake should I avoid?
```

## Small experiments

Add these to `notes.md`:

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

---

# Common Mistakes to Watch For

## Using `=` Instead of `==`

Incorrect:

```python
car = "bmw"

if car = "bmw":
    print("This is a BMW.")
```

Correct:

```python
car = "bmw"

if car == "bmw":
    print("This is a BMW.")
```

---

## Using JavaScript Operators in Python

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

---

## Forgetting Capitalized Booleans

Incorrect:

```python
is_active = true
```

Correct:

```python
is_active = True
```

Incorrect:

```python
is_active = false
```

Correct:

```python
is_active = False
```

---

## Forgetting the Colon

Incorrect:

```python
if age >= 18
    print("You can vote.")
```

Correct:

```python
if age >= 18:
    print("You can vote.")
```

---

## Checking Too Much with `elif`

Independent `if` statements are all checked:

```python
favorite_fruits = ["banana", "apple", "mango"]

if "banana" in favorite_fruits:
    print("You like bananas.")

if "apple" in favorite_fruits:
    print("You like apples.")
```

An `if-elif-else` chain stops after the first true condition:

```python
favorite_fruits = ["banana", "apple", "mango"]

if "banana" in favorite_fruits:
    print("You like bananas.")
elif "apple" in favorite_fruits:
    print("You like apples.")
```

Use independent `if` statements when more than one condition can be true.

---

# Suggested Workflow

For each exercise:

1. Read the task.
2. Predict the result before running the code.
3. Write the code.
4. Run the file.
5. Fix syntax or logic errors.
6. Explain why the condition is `True` or `False`.
7. Review indentation and spacing.
8. Commit after a meaningful group of exercises.

Run an exercise:

```bash
python3 python/python-crash-course/chapter-05-if-statements-exercises/exercise_5_1_conditional_tests.py
```

Suggested commits:

```bash
git add .
git commit -m "Complete Chapter 5 conditional test exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 5 list condition exercises"
git push
```

```bash
git add .
git commit -m "Add Chapter 5 notes and docs practice"
git push
```

---

# Chapter 5 Completion Checklist

Mark each exercise when completed.

- [x] 5-1 Conditional Tests
- [x] 5-2 More Conditional Tests
- [x] 5-3 Alien Colors #1
- [x] 5-4 Alien Colors #2
- [x] 5-5 Alien Colors #3
- [x] 5-6 Stages of Life
- [x] 5-7 Favorite Fruit
- [x] 5-8 Hello Admin
- [x] 5-9 No Users
- [x] 5-10 Checking Usernames
- [x] 5-11 Ordinal Numbers
- [x] 5-12 Styling if Statements
- [x] 5-13 Your Ideas

---

# Self-Review Questions

Answer these after finishing the chapter.

## Booleans and Comparisons

1. What is a boolean?
- A boolean is a value that represents one of two possible states: `True` or `False`.

2. What values do `True` and `False` represent?
- `True` represents that a condition is correct or active.
- `False` represents that a condition is incorrect or inactive.

Example:

```python
is_active = True
is_finished = False
```

3. What is the difference between `=` and `==`?
- `=` assigns a value to a variable.
- `==` compares two values and returns `True` or `False`.

Example:

```python
age = 18        # assignment
age == 18       # comparison
```

4. What does `!=` mean?
- `!=` means “not equal to.”
- It returns `True` when two values are different.

Example:

```python
car = "bmw"

car != "audi"  # True
```

5. What does `age >= 18` return?
- It returns a boolean: either `True` or `False`.

Example:

```python
age = 20

age >= 18  # True
```

---

## if Statements

6. What does an `if` statement do?
- An `if` statement runs a block of code only when its condition is `True`.

Example:

```python
age = 19

if age >= 18:
    print("You are old enough to vote.")
```

7. Why does indentation matter in an `if` statement?
- Indentation tells Python which lines belong inside the `if` block.
- Only the indented lines run when the condition is `True`.

Example:

```python
if age >= 18:
    print("You are old enough to vote.")
    print("Have you registered yet?")
```

8. What happens if the condition is false?
- If the condition is false, Python skips the indented block.
- If there is an `else` block, Python runs the `else` block instead.

Example:

```python
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")
```

---

## if-else and if-elif-else

9. When should I use `if-else`?
- Use `if-else` when there are two possible paths.

Example:

```python
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")
```

10. When should I use `if-elif-else`?
- Use `if-elif-else` when there are more than two possible outcomes.

Example:

```python
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
```

11. Why does order matter in an `if-elif-else` chain?
- Python checks conditions from top to bottom.
- It runs the first block whose condition is `True` and skips the rest.
- More specific or lower-range conditions often need to come before broader ones.

Example:

```python
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
```

12. Why might I omit the final `else` block?
- You might omit `else` when every condition should be explicit.
- This can make the code clearer and help avoid catching unexpected cases too broadly.

Example:

```python
if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
elif alien_color == "red":
    points = 15
```

---

## Logical Operators

13. What does `and` require to return `True`?
- `and` requires both sides to be true.

Example:

```python
age = 25

age >= 18 and age < 65  # True
```

14. What does `or` require to return `True`?
- `or` requires at least one side to be true.

Example:

```python
age = 70

age < 18 or age >= 65  # True
```

15. What does `not` do?
- `not` reverses a truth value.
- `not True` becomes `False`.
- `not False` becomes `True`.

Example:

```python
is_active = False

not is_active  # True
```

---

## Lists and Conditions

16. What does `item in items` check?
- It checks whether `item` exists inside `items`.

Example:

```python
favorite_fruits = ["banana", "apple", "mango"]

"banana" in favorite_fruits  # True
```

17. What does `item not in items` check?
- It checks whether `item` does not exist inside `items`.

Example:

```python
favorite_fruits = ["banana", "apple", "mango"]

"kiwi" not in favorite_fruits  # True
```

18. Why does `if requested_toppings:` work?
- Python treats a non-empty list as `True`.
- Python treats an empty list as `False`.

Example:

```python
requested_toppings = ["mushrooms"]

if requested_toppings:
    print("Adding toppings.")
```

19. What does an empty list evaluate to in a conditional?
- An empty list evaluates to `False`.

Example:

```python
requested_toppings = []

if requested_toppings:
    print("Adding toppings.")
else:
    print("No toppings requested.")
```

20. Why did Exercise 5-7 use independent `if` statements instead of `elif`?
- Independent `if` statements are all checked.
- This is needed because more than one favorite fruit can be in the list.
- An `if-elif-else` chain would stop after the first true condition.

Example:

```python
if "banana" in favorite_fruits:
    print("You really like bananas!")

if "apple" in favorite_fruits:
    print("You really like apples!")
```

---

## Case-Insensitive Checks

21. Why do we use `.lower()` when checking usernames?
- `.lower()` makes the comparison case-insensitive.
- It helps treat `"Admin"`, `"ADMIN"`, and `"admin"` as the same username.

Example:

```python
username = "Admin"

username.lower() == "admin"  # True
```

22. Why should we create a lowercase copy of `current_users`?
- A lowercase copy lets us compare all usernames in the same format.
- It avoids missing duplicates because of capitalization differences.

Example:

```python
current_users = ["admin", "Jaden", "Ada"]
current_users_lower = [user.lower() for user in current_users]
```

23. What could go wrong if we compare usernames without normalizing case?
- The program might allow duplicate usernames with different capitalization.

Example:

```python
"Admin" == "admin"  # False
```

Without normalization, `"Admin"` and `"admin"` could be treated as different users.

---

## Style and Review

24. What should I check when reviewing conditional tests?
- Check that comparison operators are correct.
- Check that `=` and `==` are not confused.
- Check indentation.
- Check spaces around operators.
- Check that condition order makes sense.
- Check whether independent `if` statements or an `if-elif-else` chain is the better choice.
- Check that output messages are readable.

25. Which JavaScript habits should I avoid in Python conditionals?
- Avoid JavaScript boolean operators like `&&`, `||`, and `!`.
- Avoid braces `{}` for code blocks.
- Avoid lowercase booleans like `true` and `false`.
- Avoid JavaScript template literals.
- Use Python’s `and`, `or`, `not`, indentation, `True`, `False`, and f-strings.

Example:

```python
age = 25

if age >= 18 and age < 65:
    print(f"Age: {age}")
```

---

# Key Takeaways

- A conditional test evaluates to `True` or `False`.
- Use `==` to compare values.
- Use `=` to assign values.
- Use `!=` to check inequality.
- Python uses `and`, `or`, and `not`.
- Python does not use `&&`, `||`, or `!` for boolean logic.
- `if` statements run code only when a condition is true.
- `else` handles the alternative case.
- `elif` handles additional conditions.
- `if-elif-else` chains stop at the first true condition.
- Independent `if` statements are all checked.
- `in` checks whether an item is in a list.
- `not in` checks whether an item is not in a list.
- Empty lists evaluate to `False`.
- Non-empty lists evaluate to `True`.
- `.lower()` helps make case-insensitive comparisons.
