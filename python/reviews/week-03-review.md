Week: 3 Review  
Week: 3  
Dates: May 8 - May 19  
Total hours studied: 24  

What I studied:
- Python conditionals and boolean logic
- Comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Membership checks with `in`
- Difference between `==` and `is`
- Clean boolean-return functions
- Helper functions
- Reading Exercism test results
- String methods and slicing
- List indexing and slicing
- `join()`, `split()`, `removesuffix()`, and `endswith()`
- Loops, modulo `%`, and range-based factor checking
- Raising `ValueError` with a clear error message

Exercises completed:
- Week 3 comparison and conditional practice
- Darts scoring function
- Perfect Numbers classification logic
- Little Sister’s Vocabulary string transformation functions
- Black Jack review and flashcards

Exercism exercises completed:
- Black Jack — 6 tests passed
- Darts — 13 tests passed
- Perfect Numbers — 14 tests passed
- Little Sister’s Vocabulary — 7 tests passed

Book chapters/sections completed:
- Python Crash Course Chapter 5 skill area: if statements, comparisons, booleans, and conditionals
- Continued review of earlier list, loop, slicing, and string fundamentals from Chapters 3–4

What transferred easily from JavaScript:
- Basic comparison logic
- `if` statements
- Boolean thinking with `and` / `or`
- Working with lists/arrays conceptually
- Using helper functions to avoid repeated logic
- Returning values from functions
- Breaking a problem into smaller steps

What felt different in Python:
- Using `elif` instead of `else if`
- Using `is` only for identity checks, especially `is None`
- Python slicing syntax like `word[:-4]`
- `range(1, number)` stopping before `number`
- Python’s clean direct boolean returns
- Python string methods such as `.removesuffix()` and `.endswith()`
- List comprehensions
- Exercism’s pytest warnings for custom task markers

Bugs I fixed:
- Compared card labels instead of card values in Black Jack
- Used `or` where `and` was needed for blackjack detection
- Used `is` instead of `==` for value comparison
- Checked individual cards instead of total value for double down
- Initially hardcoded `"en"` in `make_word_groups()` instead of using the dynamic prefix
- Repeated slicing logic in `remove_suffix_ness()` before refactoring with a `root` variable
- Learned to avoid checking broad conditions before specific ones, especially in Darts

Code I refactored:
- Black Jack helper logic with `value_of_card()`
- `is_blackjack()` using `has_ace and has_ten_card`
- `can_split_pairs()` using value comparison
- `can_double_down()` using total membership check
- Darts condition order from inner radius to outer radius
- Perfect Numbers using an `aliquot_sum()` helper
- `remove_suffix_ness()` using a clearer `root` variable
- `adjective_to_verb()` using `split()`, indexing, and `removesuffix()`

Main thing I understand better now:
- I understand how to translate plain-English rules into Python conditions.
- I understand that comparisons already return `True` or `False`, so many functions can return the comparison directly.
- I understand why condition order matters when multiple conditions can be true.
- I understand how helper functions make the main function cleaner and easier to test.

Main thing that still feels weak:
- Remembering when to use `and` vs `or`
- Remembering when to use `==` vs `is`
- Reading test failures quickly without getting distracted by warnings
- Choosing the cleanest condition order
- Knowing when to use a helper function
- String slicing without needing to slow down and count indexes

Questions for review:
- When should I use `and` instead of `or`?
- When should I use `is`, and why should I usually avoid it for normal value comparison?
- Why does `range(1, number)` exclude `number`?
- When is a direct boolean return better than an `if/else`?
- When should I create a helper function?
- What is the best way to read a pytest failure?
- When should I use slicing versus a string method like `.removesuffix()`?

Next week’s focus:
- Continue Python Crash Course Chapter 6: dictionaries
- Practice dictionary creation, lookup, updates, and looping
- Connect dictionaries to Django template context later
- Continue Exercism practice with dictionaries and conditionals
- Keep writing clean helper functions
- Add flashcards for repeated mistakes
- Practice reading tests and debugging failures
- Continue using Git commits after each completed exercise