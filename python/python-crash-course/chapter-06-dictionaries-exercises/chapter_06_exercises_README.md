# Python Crash Course — Chapter 6 Exercises

## Chapter 6 — Dictionaries

This folder contains practice exercises for **Python Crash Course Chapter 6: Dictionaries**.

The goal of this chapter is to learn how to:

- create dictionaries
- understand key-value pairs
- access values by key
- add new key-value pairs
- modify existing values
- delete key-value pairs
- use `.get()` for safer lookups
- loop through dictionaries
- loop through `.items()`
- loop through `.keys()`
- loop through `.values()`
- use `in` with dictionary keys
- store lists inside dictionaries
- store dictionaries inside lists
- store dictionaries inside dictionaries
- format dictionary output clearly
- connect dictionaries to Django-style data later
- continue reading official Python documentation

Recommended folder:

```text
python/python-crash-course/chapter-06-dictionaries-exercises
```

Recommended files:

```text
README.md
exercise_6_1_person.py
exercise_6_2_favorite_numbers.py
exercise_6_3_glossary.py
exercise_6_4_glossary_2.py
exercise_6_5_rivers.py
exercise_6_6_polling.py
exercise_6_7_people.py
exercise_6_8_pets.py
exercise_6_9_favorite_places.py
exercise_6_10_favorite_numbers.py
exercise_6_11_cities.py
exercise_6_12_extensions.md
```

---

# Example — Simple Dictionary

## Task

Create a dictionary that stores information about one alien.

## Concepts

- dictionary
- key-value pair
- accessing values by key
- f-strings

## Starter code

```python
alien_0 = {"color": "green", "points": 5}
```

<details>
<summary>Show starter code</summary>

```python
alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

print(f"You just earned {alien_0['points']} points!")
```

</details>

## Goal

Understand that a dictionary stores labeled values and lets you access each value by its key.

---

# Example — Adding and Modifying Values

## Task

Add new keys to a dictionary and modify an existing value.

## Concepts

- adding key-value pairs
- modifying values
- mutation

## Starter code

```python
alien_0 = {"color": "green", "points": 5}
```

<details>
<summary>Show starter code</summary>

```python
alien_0 = {"color": "green", "points": 5}

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

alien_0["color"] = "yellow"

print(f"The alien is now {alien_0['color']}.")
```

</details>

## Goal

Understand that assigning to a dictionary key can add a new key or update an existing key.

---

# Example — Looping Through a Dictionary

## Task

Loop through all key-value pairs in a dictionary.

## Concepts

- `.items()`
- key-value pairs
- `for` loops
- readable output

## Starter code

```python
user = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
```

<details>
<summary>Show starter code</summary>

```python
user = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

</details>

## Goal

Understand that `.items()` gives you both the key and the value during each loop.

---

# Exercise 6-1 — Person

## Task

Use a dictionary to store information about a person you know.

Store their:

- first name
- last name
- age
- city

Use keys such as:

```python
"first_name"
"last_name"
"age"
"city"
```

Print each piece of information stored in your dictionary.

## Concepts

- dictionaries
- key-value pairs
- accessing values by key
- readable output

## Starter code

```python
person = {
    "first_name": "",
    "last_name": "",
    "age": 0,
    "city": "",
}
```

<details>
<summary>Show starter code</summary>

```python
person = {
    "first_name": "ada",
    "last_name": "lovelace",
    "age": 36,
    "city": "london",
}

print(person["first_name"].title())
print(person["last_name"].title())
print(person["age"])
print(person["city"].title())
```

</details>

## Goal

Practice creating a dictionary and accessing each value by its key.

---

# Exercise 6-2 — Favorite Numbers

## Task

Use a dictionary to store people's favorite numbers.

Steps:

1. Think of five names.
2. Use the names as keys in your dictionary.
3. Store one favorite number for each person.
4. Print each person's name and favorite number.

For extra practice, poll a few friends and use real data.

## Concepts

- dictionaries
- names as keys
- numbers as values
- f-strings

## Starter code

```python
favorite_numbers = {
    "ada": 7,
}
```

<details>
<summary>Show starter code</summary>

```python
favorite_numbers = {
    "ada": 7,
    "guido": 42,
    "grace": 9,
    "linus": 3,
    "margaret": 11,
}

print(f"Ada's favorite number is {favorite_numbers['ada']}.")
print(f"Guido's favorite number is {favorite_numbers['guido']}.")
print(f"Grace's favorite number is {favorite_numbers['grace']}.")
print(f"Linus's favorite number is {favorite_numbers['linus']}.")
print(f"Margaret's favorite number is {favorite_numbers['margaret']}.")
```

</details>

## Goal

Practice storing related data in a dictionary and printing values by key.

---

# Exercise 6-3 — Glossary

## Task

Use a dictionary to model a small programming glossary.

Steps:

1. Think of five programming words you learned in previous chapters.
2. Use each word as a key.
3. Store each meaning as a value.
4. Print each word and its meaning as neatly formatted output.
5. Use `\n` to insert a blank line between each word-meaning pair.

## Concepts

- dictionaries
- strings
- formatting
- newline character `\n`
- repeated print statements

## Starter code

```python
glossary = {
    "variable": "A name that refers to a value.",
}
```

<details>
<summary>Show starter code</summary>

```python
glossary = {
    "variable": "A name that refers to a value.",
    "list": "An ordered collection of values.",
    "loop": "A way to repeat code.",
    "string": "Text data surrounded by quotes.",
    "boolean": "A value that is either True or False.",
}

print(f"Variable:\n\t{glossary['variable']}\n")
print(f"List:\n\t{glossary['list']}\n")
print(f"Loop:\n\t{glossary['loop']}\n")
print(f"String:\n\t{glossary['string']}\n")
print(f"Boolean:\n\t{glossary['boolean']}\n")
```

</details>

## Goal

Practice using a dictionary to connect terms with definitions.

---

# Exercise 6-4 — Glossary 2

## Task

Clean up your code from Exercise 6-3.

Steps:

1. Replace repeated `print()` calls with a loop.
2. Loop through the dictionary's keys and values.
3. Add five more Python terms.
4. Run the program again.
5. The new terms should automatically appear in the output.

## Concepts

- dictionaries
- `.items()`
- loops
- reducing repeated code
- refactoring

## Starter code

```python
glossary = {
    "variable": "A name that refers to a value.",
    "list": "An ordered collection of values.",
}
```

<details>
<summary>Show starter code</summary>

```python
glossary = {
    "variable": "A name that refers to a value.",
    "list": "An ordered collection of values.",
    "loop": "A way to repeat code.",
    "string": "Text data surrounded by quotes.",
    "boolean": "A value that is either True or False.",
    "dictionary": "A collection of key-value pairs.",
    "key": "A label used to access a value in a dictionary.",
    "value": "Data stored under a key.",
    "method": "A function attached to an object.",
    "condition": "An expression that evaluates to True or False.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")
```

</details>

## Goal

Understand how loops reduce repeated dictionary access and make programs easier to extend.

---

# Exercise 6-5 — Rivers

## Task

Make a dictionary containing three major rivers and the country each river runs through.

One key-value pair might be:

```python
"nile": "egypt"
```

Then:

1. Use a loop to print a sentence about each river.
2. Use a loop to print the name of each river.
3. Use a loop to print the name of each country.

## Concepts

- dictionaries
- `.items()`
- `.keys()`
- `.values()`
- loops
- formatted strings

## Starter code

```python
rivers = {
    "nile": "egypt",
}
```

<details>
<summary>Show starter code</summary>

```python
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "danube": "germany",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())
```

</details>

## Goal

Practice choosing `.items()`, `.keys()`, or `.values()` based on what the loop needs.

---

# Exercise 6-6 — Polling

## Task

Use the code in `favorite_languages.py`.

Steps:

1. Make a list of people who should take the favorite languages poll.
2. Include some names that are already in the dictionary.
3. Include some names that are not in the dictionary.
4. Loop through the list of people who should take the poll.
5. If they have already taken the poll, print a thank-you message.
6. If they have not taken the poll, invite them to take it.

## Concepts

- dictionaries
- lists
- `in`
- `not in`
- membership checks
- conditionals
- loops

## Starter code

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

people_to_poll = ["jen", "sarah", "erin", "phil", "ada"]
```

<details>
<summary>Show starter code</summary>

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

people_to_poll = ["jen", "sarah", "erin", "phil", "ada"]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding.")
    else:
        print(f"{person.title()}, please take our poll.")
```

</details>

## Goal

Practice checking whether a name exists as a key in a dictionary.

---

# Exercise 6-7 — People

## Task

Start with the program you wrote for Exercise 6-1.

Steps:

1. Make two new dictionaries representing different people.
2. Store all three dictionaries in a list called `people`.
3. Loop through your list of people.
4. Print everything you know about each person.

## Concepts

- dictionaries
- list of dictionaries
- loops
- nested data
- formatting output

## Starter code

```python
person_1 = {
    "first_name": "",
    "last_name": "",
    "age": 0,
    "city": "",
}

people = [person_1]
```

<details>
<summary>Show starter code</summary>

```python
person_1 = {
    "first_name": "ada",
    "last_name": "lovelace",
    "age": 36,
    "city": "london",
}

person_2 = {
    "first_name": "grace",
    "last_name": "hopper",
    "age": 85,
    "city": "new york",
}

person_3 = {
    "first_name": "alan",
    "last_name": "turing",
    "age": 41,
    "city": "manchester",
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nName: {full_name.title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
```

</details>

## Goal

Practice storing multiple dictionaries inside a list and looping through them.

---

# Exercise 6-8 — Pets

## Task

Make several dictionaries where each dictionary represents a different pet.

For each pet, include:

- kind of animal
- owner's name

Store these dictionaries in a list called `pets`.

Loop through the list and print everything you know about each pet.

## Concepts

- dictionaries
- list of dictionaries
- loops
- nested data
- readable output

## Starter code

```python
pet_1 = {
    "animal": "",
    "owner": "",
}

pets = [pet_1]
```

<details>
<summary>Show starter code</summary>

```python
pet_1 = {
    "animal": "dog",
    "owner": "ada",
}

pet_2 = {
    "animal": "cat",
    "owner": "grace",
}

pet_3 = {
    "animal": "parrot",
    "owner": "alan",
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print("\nPet information:")
    print(f"Animal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")
```

</details>

## Goal

Practice representing real-world objects as dictionaries and grouping them in a list.

---

# Exercise 6-9 — Favorite Places

## Task

Make a dictionary called `favorite_places`.

Steps:

1. Think of three names to use as keys.
2. Store one to three favorite places for each person.
3. Loop through the dictionary.
4. Print each person's name and their favorite places.

To make the exercise more interesting, ask friends for real favorite places.

## Concepts

- dictionary
- list inside a dictionary
- `.items()`
- nested loop
- formatting output

## Starter code

```python
favorite_places = {
    "ada": ["london"],
}
```

<details>
<summary>Show starter code</summary>

```python
favorite_places = {
    "ada": ["london", "paris"],
    "grace": ["new york", "boston"],
    "alan": ["manchester", "cambridge"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")

    for place in places:
        print(f"\t{place.title()}")
```

</details>

## Goal

Practice looping through a dictionary where each value is a list.

---

# Exercise 6-10 — Favorite Numbers

## Task

Modify your program from Exercise 6-2 so each person can have more than one favorite number.

Steps:

1. Store each person's favorite numbers in a list.
2. Print each person's name.
3. Print all of their favorite numbers.

## Concepts

- dictionary
- list as a value
- `.items()`
- nested loop
- formatting output

## Starter code

```python
favorite_numbers = {
    "ada": [7, 11],
}
```

<details>
<summary>Show starter code</summary>

```python
favorite_numbers = {
    "ada": [7, 11],
    "guido": [42, 3],
    "grace": [9, 14],
    "linus": [3, 8],
    "margaret": [11, 21],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")

    for number in numbers:
        print(f"\t{number}")
```

</details>

## Goal

Practice using lists as dictionary values.

---

# Exercise 6-11 — Cities

## Task

Make a dictionary called `cities`.

Steps:

1. Use the names of three cities as keys.
2. Create a dictionary of information about each city.
3. Include:
   - country
   - approximate population
   - one fact
4. Print the name of each city and all the information stored about it.

The keys for each city's dictionary should be something like:

```python
"country"
"population"
"fact"
```

## Concepts

- dictionary inside a dictionary
- nested dictionaries
- `.items()`
- readable formatting
- structured data

## Starter code

```python
cities = {
    "athens": {
        "country": "greece",
        "population": 3000000,
        "fact": "It is one of the world's oldest cities.",
    },
}
```

<details>
<summary>Show starter code</summary>

```python
cities = {
    "athens": {
        "country": "greece",
        "population": 3000000,
        "fact": "It is one of the world's oldest cities.",
    },
    "london": {
        "country": "united kingdom",
        "population": 9000000,
        "fact": "It is located on the River Thames.",
    },
    "tokyo": {
        "country": "japan",
        "population": 37000000,
        "fact": "It is one of the largest metropolitan areas in the world.",
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {city_info['country'].title()}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact']}")
```

</details>

## Goal

Practice working with nested dictionaries, which are important for representing structured data.

---

# Exercise 6-12 — Extensions

## Task

Choose one example program from this chapter and extend it.

Possible extension ideas:

- add new keys and values
- change the context of the program
- improve the formatting of the output
- add another nested list
- add another nested dictionary
- use `.get()` for safer lookups
- sort output with `sorted()`
- remove duplicate output with `set()`

## Concepts

- extending existing code
- refactoring
- formatting
- nested data
- developer thinking

## Starter code

```text
Choose one Chapter 6 program to extend.
```

<details>
<summary>Show starter code</summary>

```markdown
# Exercise 6-12 — Extensions

## Program chosen

## What I changed

## Why I changed it

## What I learned

## Next improvement
```

</details>

## Goal

Start thinking beyond copying examples by improving or extending a working program.

---

# Official Docs Practice

Chapter 6 introduces dictionaries, so official documentation practice should focus on Python's mapping type: `dict`.

Read selectively. Do not try to understand the entire documentation page at once.

## Docs sections to inspect

```text
Mapping Types — dict
Dictionary View Objects
Membership Test Operations
```

Use this checklist:

```text
1. What problem does this feature solve?
2. What syntax does it use?
3. What does it return?
4. Does it mutate the original dictionary?
5. Can it raise an error?
6. Can I run one tiny example?
7. What mistake should I avoid?
```

## Small experiments

Add these to `notes.md` or `docs_practice.py`:

```python
user = {
    "name": "Ada",
    "role": "admin",
}

print(user["name"])
print(user.get("name"))
print(user.get("active"))
print(user.get("active", False))

print("name" in user)
print("active" in user)

print(user.keys())
print(user.values())
print(user.items())

user["active"] = True
print(user)
```

## Beginner rule to extract

```text
Use square brackets when the key must exist.
Use .get() when the key might be missing.
Use .items() when you need both the key and value.
Use .keys() when you only need keys.
Use .values() when you only need values.
```

---

# Common Mistakes to Watch For

## Using a Missing Key with Square Brackets

Incorrect:

```python
user = {"name": "Ada"}

print(user["age"])
```

This causes a `KeyError` because `"age"` is not in the dictionary.

Correct:

```python
user = {"name": "Ada"}

print(user.get("age", "Age not provided."))
```

---

## Confusing Keys and Values

Incorrect:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
}

for language in favorite_languages:
    print(language.title())
```

This prints the keys, not the values.

Correct:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
}

for language in favorite_languages.values():
    print(language.title())
```

---

## Forgetting `.items()` When You Need Both Key and Value

Incorrect:

```python
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
}

for river, country in rivers:
    print(f"The {river.title()} runs through {country.title()}.")
```

Correct:

```python
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
```

---

## Hardcoding a Key Instead of Using the Loop Variable

Incorrect:

```python
people = [
    {"first_name": "ada", "last_name": "lovelace"},
    {"first_name": "grace", "last_name": "hopper"},
]

for person in people:
    print(people[0]["first_name"])
```

Correct:

```python
people = [
    {"first_name": "ada", "last_name": "lovelace"},
    {"first_name": "grace", "last_name": "hopper"},
]

for person in people:
    print(person["first_name"])
```

---

## Using a List When a Dictionary Would Be Clearer

Less clear:

```python
person = ["ada", "lovelace", 36, "london"]
```

Clearer:

```python
person = {
    "first_name": "ada",
    "last_name": "lovelace",
    "age": 36,
    "city": "london",
}
```

---

## Forgetting That Dictionary Keys Must Be Unique

Incorrect:

```python
person = {
    "name": "Ada",
    "name": "Grace",
}
```

Correct:

```python
person = {
    "first_name": "Ada",
    "last_name": "Lovelace",
}
```

---

# Suggested Workflow

For each exercise:

1. Read the task.
2. Identify the dictionary keys and values.
3. Write the starter dictionary.
4. Predict what each lookup or loop should output.
5. Write the code.
6. Run the file.
7. Fix syntax or logic errors.
8. Improve formatting.
9. Explain what the dictionary stores.
10. Commit after a meaningful group of exercises.

Run an exercise:

```bash
python3 python/python-crash-course/chapter-06-dictionaries-exercises/exercise_6_1_person.py
```

Suggested commits:

```bash
git add .
git commit -m "Complete Chapter 6 basic dictionary exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 6 dictionary loop exercises"
git push
```

```bash
git add .
git commit -m "Complete Chapter 6 nested dictionary exercises"
git push
```

```bash
git add .
git commit -m "Add Chapter 6 notes and docs practice"
git push
```

---

# Chapter 6 Completion Checklist

Mark each exercise when completed.

- [ ] 6-1 Person
- [ ] 6-2 Favorite Numbers
- [ ] 6-3 Glossary
- [ ] 6-4 Glossary 2
- [ ] 6-5 Rivers
- [ ] 6-6 Polling
- [ ] 6-7 People
- [ ] 6-8 Pets
- [ ] 6-9 Favorite Places
- [ ] 6-10 Favorite Numbers
- [ ] 6-11 Cities
- [ ] 6-12 Extensions

---

# Self-Review Questions

Answer these after finishing the chapter.

## Dictionaries

1. What is a dictionary?
- A dictionary is a collection of key-value pairs. Each key points to a related value.

2. What is a key?
- A key is the label used to access a value in a dictionary.

3. What is a value?
- A value is the data stored under a key.

4. How is a dictionary different from a list?
- A list stores ordered items by position, accessed with indexes.
- A dictionary stores labeled data by key, accessed with key names.

Example:

```python
languages = ["python", "javascript", "sql"]
person = {"first_name": "ada", "age": 36}
```

5. When should I use a dictionary instead of a list?
- Use a dictionary when each piece of data needs a meaningful label.

Example:

```python
person = {
    "first_name": "ada",
    "last_name": "lovelace",
    "age": 36,
    "city": "london",
}
```

---

## Accessing and Changing Data

6. How do I access a value by key?
- Use square brackets with the key.

```python
person["first_name"]
```

7. What happens if I use square brackets with a missing key?
- Python raises a `KeyError`.

Example:

```python
person = {"first_name": "ada"}

print(person["age"])  # KeyError
```

8. How does `.get()` help avoid `KeyError`?
- `.get()` returns `None` or a default value when the key does not exist instead of raising `KeyError`.

Example:

```python
person = {"first_name": "ada"}

print(person.get("age"))
print(person.get("age", "Age not provided."))
```

9. How do I add a new key-value pair?
- Assign a value to a new key.

```python
person["city"] = "athens"
```

10. How do I update an existing value?
- Assign a new value to an existing key.

```python
person["city"] = "london"
```

11. How do I delete a key-value pair?
- Use `del` with the key.

```python
del person["city"]
```

---

## Looping Through Dictionaries

12. What does `.items()` give me?
- `.items()` gives key-value pairs.
- Use it when each loop needs both the key and the value.

```python
for key, value in person.items():
    print(key, value)
```

13. What does `.keys()` give me?
- `.keys()` gives the dictionary keys.

```python
for key in person.keys():
    print(key)
```

14. What does `.values()` give me?
- `.values()` gives the dictionary values.

```python
for value in person.values():
    print(value)
```

15. When should I use `.items()` instead of `.keys()`?
- Use `.items()` when the loop needs both the key and the value.
- Use `.keys()` when the loop only needs keys.

Example:

```python
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
```

16. What does `for key in dictionary:` loop through by default?
- It loops through the dictionary’s keys by default.

```python
for key in person:
    print(key)
```

---

## Membership Checks

17. What does `"name" in user` check?
- It checks whether `"name"` exists as a key in the `user` dictionary.

```python
user = {"name": "Ada"}

"name" in user  # True
```

18. Does `in` check keys or values by default in a dictionary?
- It checks keys by default.

19. How would I check whether a value exists in a dictionary?
- Use `.values()`.

```python
"Ada" in user.values()
```

---

## Nesting

20. What is a list of dictionaries?
- A list of dictionaries is a list where each item is a dictionary.
- This is useful when storing several similar records.

Example:

```python
people = [
    {"first_name": "ada", "age": 36},
    {"first_name": "grace", "age": 85},
]
```

21. What is a list inside a dictionary?
- It is a dictionary where one or more values are lists.

Example:

```python
favorite_places = {
    "ada": ["london", "paris"],
    "grace": ["new york", "boston"],
}
```

22. What is a dictionary inside a dictionary?
- It is a dictionary where one or more values are other dictionaries.

Example:

```python
cities = {
    "athens": {
        "country": "greece",
        "population": 3000000,
    },
}
```

23. Why does nested data need clear variable names?
- Clear names help you understand which level of the structure you are working with.

Example:

```python
for city, city_info in cities.items():
    print(city)
    print(city_info["country"])
```

Here, `city` is the outer key and `city_info` is the inner dictionary.

---

## Style and Review

24. Why should output formatting be clean in these exercises?
- Clean formatting makes nested data easier to read, test, and debug.
- It also helps the user understand the output without needing to inspect the code.

25. Which JavaScript habits should I avoid when writing Python dictionaries?
- Avoid JavaScript object syntax habits such as:
  - using braces for code blocks
  - using `let` or `const`
  - using JavaScript template literals
  - adding unnecessary semicolons
  - forgetting Python indentation
- In Python, use dictionaries, indentation, f-strings, and Python loop syntax.

Example:

```python
person = {
    "first_name": "ada",
    "last_name": "lovelace",
}

print(f"{person['first_name'].title()} {person['last_name'].title()}")
```

---

# Key Takeaways

- A dictionary stores key-value pairs.
- A key is a label used to access a value.
- A value is the data stored under a key.
- Use square brackets when the key should exist.
- Use `.get()` when the key might be missing.
- Assigning to a key can add or update a value.
- `del` removes a key-value pair.
- `.items()` gives key-value pairs.
- `.keys()` gives keys.
- `.values()` gives values.
- Looping over a dictionary directly loops over keys.
- `in` checks dictionary keys by default.
- A list can contain dictionaries.
- A dictionary can contain lists.
- A dictionary can contain other dictionaries.
- Nested data is useful but needs clear names and formatting.
- Dictionaries are important for Django because context data is often passed as dictionaries.
