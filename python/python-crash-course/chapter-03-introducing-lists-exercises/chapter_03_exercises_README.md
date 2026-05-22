# Python Crash Course — Chapter 3 Exercises

## Chapter 3 — Introducing Lists

This folder contains practice exercises for **Python Crash Course Chapter 3: Introducing Lists**.

The goal of this chapter is to learn how to:

- create lists
- access list elements by index
- use negative indexes
- modify list items
- add items with `append()` and `insert()`
- remove items with `del`, `pop()`, and `remove()`
- sort lists with `sort()` and `sorted()`
- reverse lists with `reverse()`
- count list items with `len()`
- avoid index errors

Recommended folder:

```text
python/python-crash-course/chapter-03-introducing-lists-exercises
```

Recommended file names:

```text
exercise_3_1_names.py
exercise_3_2_greetings.py
exercise_3_3_own_list.py
exercise_3_4_guest_list.py
exercise_3_5_changing_guest_list.py
exercise_3_6_more_guests.py
exercise_3_7_shrinking_guest_list.py
exercise_3_8_seeing_the_world.py
exercise_3_9_dinner_guests.py
exercise_3_10_every_function.py
```

---

# Exercise 3-1 — Names

## Task

Store the names of a few friends in a list called `names`.

Print each person’s name by accessing each element in the list, one at a time.

## Concepts

- list creation
- indexing
- `print()`

## Starter code

```python
names = ["ada", "eric", "guido"]
```

<details>
<summary>Show starter code</summary>

```python
print(names[0])
print(names[1])
print(names[2])
```

</details>

## Goal

Practice accessing individual list elements by index.

---

# Exercise 3-2 — Greetings

## Task

Start with the list from Exercise 3-1.

Instead of just printing each person’s name, print a personalized message to each person.

The text of each message should be the same, but each message should include the person’s name.

## Concepts

- list indexing
- f-strings
- personalized output

## Starter code

```python
names = ["ada", "eric", "guido"]
```

<details>
<summary>Show starter code</summary>

```python
print(f"Hello, {names[0].title()}!")
print(f"Hello, {names[1].title()}!")
print(f"Hello, {names[2].title()}!")
```

</details>

## Goal

Practice combining list access with f-strings.

---

# Exercise 3-3 — Your Own List

## Task

Think of your favorite mode of transportation, such as motorcycles, cars, bicycles, or trains.

Create a list that stores several examples.

Use your list to print a series of statements about these items.

## Example output

```text
I would like to own a Honda motorcycle.
```

## Concepts

- lists
- indexing
- f-strings
- meaningful variable names

## Starter code

```python
vehicles = ["Honda motorcycle", "Tesla car", "Yamaha bicycle"]
```

<details>
<summary>Show starter code</summary>

```python
print(f"I would like to own a {vehicles[0]}.")
print(f"I would like to drive a {vehicles[1]}.")
print(f"I would like to ride a {vehicles[2]}.")
```

</details>

## Goal

Practice using list values inside full sentences.

---

# Exercise 3-4 — Guest List

## Task

If you could invite anyone, living or deceased, to dinner, who would you invite?

Make a list that includes at least three people.

Print a message to each person inviting them to dinner.

## Concepts

- lists
- indexing
- f-strings
- repeated message patterns

## Starter code

```python
guests = ["Ada Lovelace", "Alan Turing", "Grace Hopper"]
```

<details>
<summary>Show starter code</summary>

```python
print(f"{guests[0]}, I would like to invite you to dinner.")
print(f"{guests[1]}, I would like to invite you to dinner.")
print(f"{guests[2]}, I would like to invite you to dinner.")
```

</details>

## Goal

Practice storing related values in a list and using each value individually.

---

# Exercise 3-5 — Changing Guest List

## Task

One of your guests cannot make the dinner, so you need to invite someone else.

Start with your program from Exercise 3-4.

Do the following:

1. Print the name of the guest who cannot make it.
2. Replace that guest with a new person.
3. Print a second set of invitation messages.

## Concepts

- modifying list elements
- indexing
- replacing values
- reusing list data

## Starter code

```python
guests = ["Ada Lovelace", "Alan Turing", "Grace Hopper"]
```

<details>
<summary>Show starter code</summary>

```python
print(f"{guests[1]} can't make it to dinner.")

guests[1] = "Katherine Johnson"

print(f"{guests[0]}, I would like to invite you to dinner.")
print(f"{guests[1]}, I would like to invite you to dinner.")
print(f"{guests[2]}, I would like to invite you to dinner.")
```

</details>

## Goal

Practice changing an item in a list by assigning a new value at a specific index.

---

# Exercise 3-6 — More Guests

## Task

You found a bigger dinner table, so now you can invite three more guests.

Start with your program from Exercise 3-4 or 3-5.

Do the following:

1. Print a message saying you found a bigger table.
2. Use `insert()` to add one guest to the beginning of the list.
3. Use `insert()` to add one guest to the middle of the list.
4. Use `append()` to add one guest to the end of the list.
5. Print a new invitation message for each person.

## Concepts

- `insert()`
- `append()`
- list growth
- indexing

## Starter code

```python
guests = ["Ada Lovelace", "Katherine Johnson", "Grace Hopper"]
```

<details>
<summary>Show starter code</summary>

```python
print("Good news! I found a bigger dinner table.")

guests.insert(0, "Guido van Rossum")
guests.insert(2, "Margaret Hamilton")
guests.append("Donald Knuth")

print(f"{guests[0]}, I would like to invite you to dinner.")
print(f"{guests[1]}, I would like to invite you to dinner.")
print(f"{guests[2]}, I would like to invite you to dinner.")
print(f"{guests[3]}, I would like to invite you to dinner.")
print(f"{guests[4]}, I would like to invite you to dinner.")
print(f"{guests[5]}, I would like to invite you to dinner.")
```

</details>

## Goal

Practice adding elements to different positions in a list.

---

# Exercise 3-7 — Shrinking Guest List

## Task

Your new dinner table will not arrive in time, so you can invite only two people.

Start with your program from Exercise 3-6.

Do the following:

1. Print a message saying you can invite only two people.
2. Use `pop()` to remove guests one at a time until only two names remain.
3. Each time you pop a name, print an apology message.
4. Print a message to each remaining guest letting them know they are still invited.
5. Use `del` to remove the final two names.
6. Print the list to confirm that it is empty.

## Concepts

- `pop()`
- `del`
- shrinking a list
- checking list contents
- list length

## Starter code

```python
guests = [
    "Guido van Rossum",
    "Ada Lovelace",
    "Margaret Hamilton",
    "Katherine Johnson",
    "Grace Hopper",
    "Donald Knuth",
]
```

<details>
<summary>Show starter code</summary>

```python
print("Sorry, I can invite only two people to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

print(f"{guests[0]}, you are still invited to dinner.")
print(f"{guests[1]}, you are still invited to dinner.")

del guests[0]
del guests[0]

print(guests)
```

</details>

## Goal

Practice removing elements from a list and understanding how the list changes.

---

# Exercise 3-8 — Seeing the World

## Task

Think of at least five places in the world you would like to visit.

Do the following:

1. Store the locations in a list.
2. Print the list in its original order.
3. Use `sorted()` to print the list in alphabetical order without modifying the original list.
4. Print the list again to show it is still in the original order.
5. Use `sorted()` to print the list in reverse alphabetical order without modifying the original list.
6. Print the list again to show it is still in the original order.
7. Use `reverse()` to change the order of the list.
8. Use `reverse()` again to restore the original order.
9. Use `sort()` to permanently sort the list alphabetically.
10. Use `sort(reverse=True)` to permanently sort the list in reverse alphabetical order.

## Concepts

- `sorted()`
- `sort()`
- `reverse()`
- original list vs modified list
- temporary sorting vs permanent sorting

## Starter code

```python
places = ["japan", "canada", "iceland", "new zealand", "peru"]
```

<details>
<summary>Show starter code</summary>

```python
print("Original list:")
print(places)

print("\nSorted list:")
print(sorted(places))

print("\nOriginal list again:")
print(places)

print("\nReverse sorted list:")
print(sorted(places, reverse=True))

print("\nOriginal list again:")
print(places)

places.reverse()
print("\nReversed list:")
print(places)

places.reverse()
print("\nBack to original order:")
print(places)

places.sort()
print("\nSorted permanently:")
print(places)

places.sort(reverse=True)
print("\nReverse sorted permanently:")
print(places)
```

</details>

## Goal

Understand the difference between temporary sorting and permanent sorting.

---

# Exercise 3-9 — Dinner Guests

## Task

Use one of your programs from Exercises 3-4 through 3-7.

Use `len()` to print a message indicating the number of people you are inviting to dinner.

## Concepts

- `len()`
- list length
- f-strings

## Starter code

```python
guests = ["Ada Lovelace", "Katherine Johnson", "Grace Hopper"]
```

<details>
<summary>Show starter code</summary>

```python
print(f"I am inviting {len(guests)} people to dinner.")
```

</details>

## Goal

Practice using `len()` to count list items.

---

# Exercise 3-10 — Every Function

## Task

Think of things you could store in a list.

Examples:

- mountains
- rivers
- countries
- cities
- languages
- foods
- books
- games

Create a list and use each list function introduced in Chapter 3 at least once.

## Required methods/functions

Use these at least once:

- access by index: `items[0]`
- negative index: `items[-1]`
- modify an item: `items[0] = "new value"`
- `append()`
- `insert()`
- `del`
- `pop()`
- `remove()`
- `sorted()`
- `sort()`
- `reverse()`
- `len()`

## Starter code

```python
languages = ["python", "javascript", "go", "rust", "java"]
```

<details>
<summary>Show starter code</summary>

```python
print(languages[0])
print(languages[-1])

languages[0] = "typescript"
languages.append("c")
languages.insert(1, "ruby")

del languages[2]

popped_language = languages.pop()
print(f"I removed {popped_language}.")

languages.remove("java")

print(sorted(languages))

languages.sort()
print(languages)

languages.reverse()
print(languages)

print(f"There are {len(languages)} languages in the list.")
```

</details>

## Goal

Practice all major Chapter 3 list operations in one program.

---

# Suggested Workflow

For each exercise:

1. Read the task.
2. Write the code from memory.
3. Run the file.
4. Fix errors.
5. Add a short comment explaining the main concept.
6. Commit after a meaningful group of exercises.

Example:

```bash
python3 python/python-crash-course/chapter-03-introducing-lists/exercise_3_1_names.py
```

Commit examples:

```bash
git add .
git commit -m "Complete Chapter 3 basic list exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 3 guest list exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 3 sorting exercises"
git push
```

---

# Chapter 3 Completion Checklist

Mark each exercise when completed.

- [x] 3-1 Names
- [x] 3-2 Greetings
- [x] 3-3 Your Own List
- [x] 3-4 Guest List
- [x] 3-5 Changing Guest List
- [x] 3-6 More Guests
- [x] 3-7 Shrinking Guest List
- [x] 3-8 Seeing the World
- [x] 3-9 Dinner Guests
- [x] 3-10 Every Function

---

# Self-Review Questions

Answer these after finishing the chapter.

## Lists and Indexing

1. What is a list?
- A list is an ordered collection of items stored in one variable.
- Lists can store strings, numbers, booleans, or other objects.

Example:

```python
languages = ["python", "javascript", "sql"]
```

2. What does index `0` mean?
- Index `0` means the first item in a list.
- Python list indexes start at `0`, not `1`.

Example:

```python
languages = ["python", "javascript", "sql"]

languages[0]  # "python"
```

3. What does index `-1` mean?
- Index `-1` means the last item in a list.

Example:

```python
languages = ["python", "javascript", "sql"]

languages[-1]  # "sql"
```

4. What happens if I access an index that does not exist?
- Python raises an `IndexError`.
- This means the list index is out of range.

Example:

```python
languages = ["python", "javascript", "sql"]

# languages[10]  # IndexError
```

---

## Modifying Lists

5. What is the difference between `append()` and `insert()`?
- `append()` adds a new item to the end of the list.
- `insert()` adds a new item at a specific index.

Example:

```python
languages = ["python", "javascript"]

languages.append("sql")
languages.insert(1, "ruby")

print(languages)
# ["python", "ruby", "javascript", "sql"]
```

6. What is the difference between `pop()` and `del`?
- `pop()` removes an item and returns it, so you can still use the removed value.
- `del` removes an item without returning it.

Example:

```python
languages = ["python", "javascript", "sql"]

removed_language = languages.pop()
print(removed_language)  # "sql"

del languages[0]
```

7. When should I use `remove()`?
- Use `remove()` when you know the value you want to remove, not its index.
- `remove()` deletes the first matching value.

Example:

```python
languages = ["python", "javascript", "sql"]

languages.remove("javascript")
```

---

## Organizing Lists

8. What is the difference between `sort()` and `sorted()`?
- `sort()` permanently changes the original list.
- `sorted()` returns a sorted version without changing the original list.

Example:

```python
places = ["japan", "canada", "iceland"]

print(sorted(places))
print(places)  # original list is unchanged

places.sort()
print(places)  # original list is now changed
```

9. What does `reverse()` do?
- `reverse()` permanently reverses the current order of the list.
- It does not sort alphabetically. It only reverses the existing order.

Example:

```python
places = ["japan", "canada", "iceland"]

places.reverse()
print(places)
# ["iceland", "canada", "japan"]
```

10. What does `len()` return?
- `len()` returns the number of items in the list.

Example:

```python
languages = ["python", "javascript", "sql"]

len(languages)  # 3
```

---

## Developer Habits

11. Did I run every file?
- Yes, each exercise file should be run from the terminal to confirm it works.

Example:

```bash
python3 python/python-crash-course/chapter-03-introducing-lists-exercises/exercise_3_1_names.py
```

12. Did I commit my completed work?
- Yes, completed work should be committed after a meaningful group of exercises.

Example:

```bash
git add .
git commit -m "Complete Chapter 3 list exercises"
git push
```

13. Can I explain every list method I used?
- You should be able to explain what each method does, whether it changes the original list, and whether it returns a useful value.

Quick review:

```text
append()  -> adds to the end, mutates the list
insert()  -> adds at an index, mutates the list
pop()     -> removes and returns an item, mutates the list
remove()  -> removes first matching value, mutates the list
sort()    -> sorts the original list, mutates the list
sorted()  -> returns a sorted copy, does not mutate the list
reverse() -> reverses the original list, mutates the list
len()     -> returns the number of items
```

---

---

# Key Takeaways

- Python lists store multiple values in one variable.
- Python list indexes start at `0`.
- Negative indexes count from the end of the list.
- `append()` adds to the end of a list.
- `insert()` adds to a specific position.
- `pop()` removes and returns an item.
- `del` removes an item without returning it.
- `remove()` deletes by value.
- `sorted()` returns a sorted copy.
- `sort()` permanently changes the list.
- `reverse()` permanently reverses the current list order.
- `len()` returns the number of items in a list.
