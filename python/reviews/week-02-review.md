# Week 2 Review

Week: Review  
Week: 2  
Dates: April 30 - May 7  
Total hours studied: 20

## What I studied

- Python Crash Course Chapter 3 — Introducing Lists
- Python Crash Course Chapter 4 — Working with Lists
- Lists, indexes, and negative indexes
- Adding, removing, modifying, and sorting list items
- `for` loops
- Loop variables
- Indentation inside and outside loops
- `range()`
- `list(range())`
- Numerical lists
- `min()`, `max()`, and `sum()`
- List comprehensions
- Slicing lists
- Copying lists with `[:]`
- Tuples
- Basic PEP 8/code review habits
- Writing pytest-style test files
- Exercism practice with loops, numbers, strings, and conditionals

## Exercises completed

- Python Crash Course Chapter 3 exercises
- Python Crash Course Chapter 4 exercises
- Week 2 custom drills
- Week 2 drill test file
- Chapter 4 `notes.md`
- Chapter 4 README self-review questions

## Exercism exercises completed

- Armstrong Numbers
- Collatz Conjecture
- Grains

## Book chapters/sections completed

- Chapter 3: Introducing Lists
- Chapter 4: Working with Lists

## What transferred easily from JavaScript

- Understanding arrays/lists as ordered collections
- Accessing items by index
- Using loops to repeat work
- Using conditionals in logic
- Thinking about functions with input and output
- Understanding the difference between debug output and returned values
- Recognizing boolean-style expressions like comparisons

## What felt different in Python

- Python uses indentation instead of curly braces
- Python uses `and` / `or` instead of `&&` / `||`
- Python uses `//` for integer division
- Python uses `**` for exponentiation
- List slicing such as `items[:3]` and `items[-3:]` felt different at first
- `range()` excludes the stop value
- `.append()` mutates the original list and returns `None`
- Copying a list needs `[:]`; assigning one list variable to another points to the same list

## Bugs I fixed

- Fixed slice explanations for `players[0:3]`, `players[:3]`, and `players[-3:]`
- Fixed list copying misunderstanding: `items[:]` creates a copy, but `items` refers to the original list
- Fixed `last_items()` naming to `last_item()`
- Fixed Collatz loop bug where the new number was calculated but not assigned back to `number`
- Fixed Collatz return value so it returns an integer instead of a formatted string
- Fixed Python syntax mistake from JavaScript: used `or` instead of `&&`
- Fixed Grains formula from linear multiplication to exponentiation with `2 ** (number - 1)`
- Removed or planned to remove debug `print()` calls before final Exercism submission
- Identified `.pyc` files as generated files that should not be committed

## Code I refactored

- Moved Week 2 drill checks into a separate test file
- Improved naming from unclear singular names to clearer plural names like `items`, `numbers`, and `words`
- Used full-slice copying with `[:]`
- Rewrote some loop-based logic using list comprehensions
- Cleaned Chapter 4 notes into a dedicated `notes.md` file
- Improved README quiz answers and self-review wording

## Main thing I understand better now

I understand how to work through lists with loops, how loop variables change on each pass, and how indentation controls what belongs inside a loop. I also understand slicing better, especially that the start index is included and the stop index is excluded.

I also understand that functions should usually return clean values, not printed messages, because returned values can be tested, reused, and submitted to Exercism.

## Main thing that still feels weak

- Knowing when to use a normal loop versus a list comprehension
- Remembering that `range()` excludes the stop value
- Avoiding JavaScript syntax habits like `&&`
- Remembering to assign updated values back to variables inside loops
- Keeping final exercise files clean by removing debug prints
- Running tests from the correct folder and understanding pytest-style test files

## Questions for review:

- When should I use a constant instead of a normal variable?
    - Use a constant when the value represents a fixed rule or configuration that should not change while the program runs.
    - Use a normal variable when the value may change during the program.

- When should I write a helper function?
    - Write a helper function when you notice repeated logic.
    - Write a helper function when one part of the program has a clear smaller job.
    - Write a helper function when naming that smaller job would make the main code easier to read.

- Is it better to use `int(amount // denomination)` or `int(amount / denomination)` in Currency Exchange?
    - It is better to use floor division with `//` when you want whole bills only.
    - `//` clearly communicates that the decimal part should be discarded.
    - It matches the problem better because you cannot receive part of a bill.

- How many tests should I write for small practice functions?
    - For a small practice function, start with two or three tests.
    - Test one normal case.
    - Test one different normal case.
    - Add one edge case if the function has an obvious edge case.

- When should I use `print()` in real code?
    - Use `print()` when you want to show information to the user.
    - Use `print()` when you are temporarily debugging or inspecting a value.
    - Do not use `print()` as the main result of a reusable function unless the function’s purpose is display.

- When should I use `return`?
    - Use `return` when a function needs to give a value back to the rest of the program.
    - Use `return` when the result needs to be tested, reused, stored, or passed into another function.

## Next week’s focus

- Python Crash Course Chapter 5 — If Statements
- Boolean values: `True` and `False`
- Comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- `if`, `elif`, and `else`
- Checking values in lists
- More Exercism practice with Bools, Conditionals, and Comparisons
- Suggested Exercism exercises: Raindrops, Darts, Bob