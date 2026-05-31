# Week 4 Review

## Week

Week: 4

## Focus

— Python Crash Course Chapter 6  
— Dictionaries  
— Python Crash Course Chapter 7  
— While-loop control flow  

## Dates

May 20 - May 31

## Total hours studied

26 hours

## What I studied

This week I studied Python dictionaries, nested data, dictionary access with `.get()`, looping through dictionary values, accumulator dictionaries, filtering lists of dictionaries, and while-loop control flow.

I also practiced how to decide whether a problem needs one loop or a nested loop. The main focus was not basic syntax, but understanding the shape of the data before choosing the loop.

Main topics:

- dictionaries
- key-value pairs
- `.get()`
- `.values()`
- list of dictionaries
- nested lists inside dictionaries
- accumulator lists
- accumulator dictionaries
- accumulator numbers
- `while` loops
- `.pop()`
- `.remove()`
- `continue`
- fallback returns
- one loop vs nested loop
- return values vs print statements
- basic edge cases

## Exercises completed

Python Crash Course:

- Chapter 6 dictionary exercises
- Chapter 7 user input and while-loop exercises

Week 4 custom drills completed:

- Drill 1 — Build a user profile dictionary
- Drill 2 — Get a city safely with `.get()`
- Drill 3 — Count favorite languages
- Drill 4 — List admin users
- Drill 5 — Move pending orders
- Drill 6 — Remove an unavailable item

Week 4 logic repair drills completed:

- Collect team names
- Collect every player
- Count players per team
- Get players for one team
- Count all players across teams
- Collect large teams
- Count player names by first letter
- Count languages from a list of dictionaries
- Collect players from large teams
- Find teams for one player
- Count player first letters across teams
- Count teams with players

## Exercism exercises completed

No new Exercism exercise was confirmed as completed during Week 4.

Most of the week was spent on Python Crash Course Chapters 6–7 and custom Week 4 drills for dictionaries, nested data, and while-loop control flow.

## Book chapters/sections completed

Completed:

- Python Crash Course Chapter 6 — Dictionaries
- Python Crash Course Chapter 7 — User Input and While Loops

Main chapter topics:

- dictionary creation
- accessing dictionary values
- using `.get()`
- looping through dictionaries
- nesting dictionaries and lists
- user input basics
- `while` loops
- moving items between lists
- removing repeated items from lists
- loop control flow

## What transferred easily from JavaScript

These ideas transferred well from JavaScript:

- objects → dictionaries
- arrays → lists
- property access idea → key lookup idea
- loops over collections
- conditionals
- building a result step by step
- using an accumulator variable
- filtering data with an `if` condition
- checking whether a value exists in a collection

The general idea of structured data was familiar from JavaScript objects and arrays.

## What felt different in Python

Python dictionaries feel similar to JavaScript objects, but the syntax and habits are different.

Things that felt different:

- using `.get()` instead of direct access when a key may be missing
- remembering that dictionary keys must match exactly
- understanding when to use `.values()` and when not to
- Python indentation controls code blocks
- `None` appears when a function has no fallback return
- `continue` skips one loop cycle, while `return` exits the whole function
- `while` loops often mutate lists with `.pop()` or `.remove()`
- Python encourages clearer, smaller functions with return values

## Bugs I fixed

Bugs fixed this week:

- Used the wrong dictionary key, such as `"Players"` instead of `"players"`.
- Used `team.get(team_name, "")` when `team_name` was a value, not a key.
- Forgot a fallback `return []` when no matching team was found.
- Appended the wrong value, such as appending `player_name` instead of the matching team name.
- Used the string literal `"language"` instead of the variable `language` when counting languages.
- Used `return` when I needed `continue`, which stopped the whole function too early.
- Used `.values()` when I only needed one specific dictionary key.
- Used the wrong default type in `.get()`, such as `""` when the expected value should be a list.
- Had difficulty deciding whether a drill needed one loop or a nested loop.

## Code I refactored

Refactors completed or identified:

- Changed extra variables into direct appends when the variable was unnecessary.
- Improved `.get()` defaults to match expected types:
  - string key → `""`
  - list key → `[]`
  - count value → `0`
- Replaced unclear variable names with clearer names.
- Changed `return` to `continue` when skipping only one invalid item.
- Used accumulator dictionaries more consistently with:

```python
counts[item] = counts.get(item, 0) + 1
```

- Improved loop reasoning by writing comments that describe the data shape:
  - list → dictionary → list → string

## Main thing I understand better now

The main thing I understand better now is that nested data does not automatically mean nested loops.

The loop choice depends on the task:

- Need one value from each dictionary → one loop.
- Need to count the length of an inner list → one loop plus `len()`.
- Need to check whether a value is inside an inner list → one loop plus `in`.
- Need every item inside an inner list → nested loop.
- Need to build a dictionary count → start with `{}` and use `.get(key, 0) + 1`.
- Need to build a list → start with `[]` and append matching values.
- Need to build a number → start with `0` and increase it.

## Main thing that still feels weak

The weakest area is still logic planning before coding.

Specific weak areas:

- identifying the data shape before writing the loop
- knowing what the loop variable contains
- deciding whether the output should be a list, dictionary, number, or boolean
- choosing one loop vs nested loop
- knowing when to return immediately and when to keep looping
- remembering to handle fallback cases
- reading nested data without getting lost

This is improving, but it still needs review.

## Questions for review

1. When should I use one loop instead of a nested loop?
2. When should I use `len(players)` instead of looping through `players`?
3. When should I use `player_name in players` instead of a nested loop?
4. What is the difference between `return` and `continue`?
5. Why does a missing fallback return cause `None`?
6. When should I use `.get()` instead of direct dictionary access?
7. How do I choose the correct default value for `.get()`?
8. What is the difference between `"language"` and `language`?
9. Why should accumulator variable names describe the stored result?
10. How do I explain a function in plain English before coding it?
11. How do dictionary drills connect to Django later?
12. What should I test for dictionary and nested-list functions?

## Review Question Answers

### 1. When should I use one loop instead of a nested loop?

Use one loop when each item in the outer collection gives you enough information to solve the task.

Examples of one-loop tasks:

- Get one value from each dictionary.
- Count how many players each team has.
- Check whether a player is inside a team's players list.
- Collect team names based on a condition.
- Count teams that have players.

Main rule:

Nested data does not automatically mean nested loops. If you only need something about the inner list, use one loop. If you need each item inside the inner list, use a nested loop.

### 2. When should I use `len(players)` instead of looping through `players`?

Use `len(players)` when you only need the number of players, not the individual player names.

Use it for questions like:

- How many players are on this team?
- Does this team have at least 2 players?
- Count all players across teams.

You do not need to loop through every player just to count them manually. Python already knows the list length.

### 3. When should I use `player_name in players` instead of a nested loop?

Use `player_name in players` when you only need to check whether a specific player exists in the list.

The question is:

Is this value inside this list?

That does not require a nested loop.

Use a nested loop only when the task asks you to process each player one by one, such as collecting all player names or counting each player's first letter.

### 4. What is the difference between `return` and `continue`?

`return` exits the whole function immediately.

`continue` skips only the current loop cycle and moves to the next item.

Use `return` when the function is finished and you have the final answer.

Use `continue` when one item is invalid or should be skipped, but the rest of the list still needs to be processed.

### 5. Why does a missing fallback return cause `None`?

In Python, if a function reaches the end without returning a value, Python automatically returns `None`.

This often happens when a function returns inside an `if` condition, but no condition matches.

For search-style functions, you often need a fallback return after the loop.

Plain English:

If I found the thing, return it. If the loop finishes and I never found it, return the default result.

### 6. When should I use `.get()` instead of direct dictionary access?

Use `.get()` when a key might be missing.

Direct dictionary access is fine when you are certain the key exists.

`.get()` is safer for messy or optional data because it avoids a crash when the key is missing.

Use `.get()` especially when working with:

- lists of dictionaries
- optional fields
- user data
- API-style data
- dictionaries where not every item has the same keys

### 7. How do I choose the correct default value for `.get()`?

Choose a default value that matches the type you expect.

Rules:

- Expected string → empty string
- Expected list → empty list
- Expected dictionary → empty dictionary
- Expected number → zero
- Expected optional value → `None`

The default should let the rest of your logic continue safely.

For example, if you expect a list of players, use an empty list as the fallback because looping over an empty list or checking its length is safe.

### 8. What is the difference between `"language"` and `language`?

`"language"` is a string literal. It means the exact text: language.

`language` is a variable. It means: use the value stored inside this variable.

This was the bug in the language-counting drill.

The output dictionary should count actual values like `"python"` or `"c"`, not the word `"language"` itself.

Main rule:

Quotes mean literal text. No quotes means variable name.

### 9. Why should accumulator variable names describe the stored result?

Accumulator variables help you track what you are building.

A good accumulator name tells you the output shape and purpose.

Examples:

- `team_names` means a list of team names.
- `language_counts` means a dictionary counting languages.
- `total_players` means a number.
- `matching_teams` means teams that matched a condition.

Bad or vague names make logic harder to debug because you forget what the variable is supposed to contain.

### 10. How do I explain a function in plain English before coding it?

Use this pattern:

1. Start with what I am building.
2. Loop through the input.
3. Get the value I need.
4. Check the condition, if there is one.
5. Add, count, return, or skip.
6. Return the final result.

Example structure in plain English:

Start with an empty result. Loop through each team. Get the players. If the team matches the condition, add the value I need to the result. After the loop, return the result.

This helps you code from logic instead of guessing syntax.

### 11. How do dictionary drills connect to Django later?

Dictionaries connect strongly to Django because Django uses structured data everywhere.

You will see similar thinking in:

- view functions
- template context
- form data
- request data
- model fields
- JSON responses
- database query results
- user/session data

A Django view often gathers data, puts it into a dictionary-like context, and sends it to a template.

So these drills are not random. They train the same skill you need later:

Understand the shape of the data, extract the right values, and pass clean results forward.

### 12. What should I test for dictionary and nested-list functions?

Test these cases:

1. Normal case  
   The function works with expected data.

2. Empty input  
   Empty list or empty dictionary.

3. Missing key  
   A dictionary does not have the expected key.

4. Empty inner list  
   A team has no players.

5. One-item inner list  
   Useful for boundary conditions.

6. Multiple matching items  
   More than one team or player should match.

7. No matches  
   The function should return the correct fallback, often an empty list, empty dictionary, zero, or `False`.

8. Repeated values  
   Useful for counting functions.

## Next week’s focus

Week 5 focus:

— Python Crash Course Chapter 8  
— Functions and clean code  
— Parameters and arguments  
— Return values  
— Default values  
— Helper functions  
— Refactoring earlier code  
— Writing cleaner, smaller functions  
— Adding simple tests  

Before fully moving into Week 5, I should do a short consolidation pass:

1. Put the Week 4 logic repair drills into a file.
2. Add simple pytest tests for the most important functions.
3. Refactor unclear variable names.
4. Review `.get()`, accumulator dictionaries, `continue`, and nested-loop decisions.
5. Commit the cleaned Week 4 files.

Main Week 5 goal:

Move from code that works to code that is readable, testable, and reusable.

## Key Takeaways

- Nested data does not automatically mean nested loops.
- Choose the loop based on the output you need.
- Use one loop when one item gives enough information.
- Use nested loops only when you need each item inside an inner collection.
- Use `.get()` when keys may be missing.
- Use `return` to finish the function.
- Use `continue` to skip one bad item and keep going.
- Explain the function in plain English before writing code.
