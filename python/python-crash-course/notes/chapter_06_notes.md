# Chapter 6 Notes — Dictionaries

These notes summarize the most important ideas from **Python Crash Course Chapter 6: Dictionaries**.

---

## What Chapter 6 Is About

Chapter 6 introduces dictionaries, one of the most important data structures in Python.

You learned how to:

```text
- create dictionaries
- understand key-value pairs
- access values by key
- add new key-value pairs
- modify existing values
- delete key-value pairs
- use .get() to avoid missing-key errors
- loop through dictionaries
- loop through keys
- loop through values
- use sorted() with dictionary keys
- use set() to remove duplicate values
- nest dictionaries and lists
```

---

## Dictionaries

A dictionary stores related information as **key-value pairs**.

Example:

```python
alien = {
    "color": "green",
    "points": 5,
}
```

In this dictionary:

```text
"color" is a key
"green" is a value

"points" is a key
5 is a value
```

A dictionary is useful when one object has multiple pieces of information.

Examples:

```text
- a user with a username, first name, last name, and location
- an alien with a color, speed, and point value
- a city with a country, population, and fact
- a programming term with a definition
```

---

## Key-Value Pairs

A key-value pair connects one label to one value.

Example:

```python
person = {
    "first_name": "ada",
    "last_name": "lovelace",
}
```

The key is used to look up the value.

```python
print(person["first_name"])  # ada
```

Use a dictionary when the data has clear labels.

Use a list when you only need an ordered collection of items.

---

## Accessing Values

Use square brackets with the key name to access a value.

Example:

```python
alien = {
    "color": "green",
    "points": 5,
}

print(alien["color"])
print(alien["points"])
```

Output:

```text
green
5
```

You can also store the value in a variable.

```python
new_points = alien["points"]
print(f"You earned {new_points} points!")
```

---

## Adding Key-Value Pairs

Dictionaries can grow while the program is running.

Example:

```python
alien = {
    "color": "green",
    "points": 5,
}

alien["x_position"] = 0
alien["y_position"] = 25

print(alien)
```

Result:

```python
{"color": "green", "points": 5, "x_position": 0, "y_position": 25}
```

Use this pattern when you start with partial information and add more data later.

---

## Starting with an Empty Dictionary

You can start with an empty dictionary and add values later

Example:

```python
user = {}

user["username"] = "mcurie"
user["first_name"] = "marie"
user["last_name"] = "curie"

print(user)
```

This is useful when data is built step by step.

Examples:

```text
- collecting user input
- generating game objects
- building data from a file
- preparing data before saving it
```

---

## Modifying Values

To change a value, assign a new value to an existing key.

Example:

```python
alien = {
    "color": "green",
}

print(f"The alien is {alien['color']}.")

alien["color"] = "yellow"

print(f"The alien is now {alien['color']}.")
```

Dictionaries are mutable, which means their contents can be changed.

---

## Using Dictionary Values in Logic

Dictionary values can control program behavior.

Example:

```python
alien = {
    "x_position": 0,
    "speed": "medium",
}

if alien["speed"] == "slow":
    x_increment = 1
elif alien["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien["x_position"] = alien["x_position"] + x_increment

print(alien["x_position"])
```

This combines:

```text
- dictionaries
- conditionals
- variables
- updating stored data
```

This is a common pattern in real programs.

---

## Removing Key-Value Pairs

Use `del` to remove a key-value pair.

Example:

```python
alien = {
    "color": "green",
    "points": 5,
}

del alien["points"]

print(alien)
```

Result:

```python
{"color": "green"}
```

Important:

```text
del permanently removes the key-value pair from that dictionary.
```

Use `del` only when you are sure the data should be removed.

---

## A Dictionary of Similar Objects

A dictionary can store similar information for many related items.

Example:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

print(favorite_languages["sarah"].title())
```

This dictionary connects each person to one favorite language.

This structure is useful when each key has the same kind of value.

---

## Formatting Larger Dictionaries

For longer dictionaries, use one key-value pair per line.

Example:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
```

This is easier to read than putting everything on one line.

A trailing comma after the last pair is acceptable and often helpful.

---

## Using `.get()`

Square bracket access causes an error if the key does not exist.

Example:

```python
alien = {
    "color": "green",
    "speed": "slow",
}

print(alien["points"])
```

This raises a `KeyError` because `"points"` is missing.

Use `.get()` when a key might not exist.

Example:

```python
alien = {
    "color": "green",
    "speed": "slow",
}

points = alien.get("points", "No point value assigned.")

print(points)
```

Output:

```text
No point value assigned.
```

The first argument is the key to look for.

The second argument is the fallback value.

```python
dictionary.get(key, fallback_value)
```

If the key exists, `.get()` returns the real value.

If the key does not exist, `.get()` returns the fallback value.

---

## `.get()` Without a Fallback

If you use `.get()` without a fallback, Python returns `None` when the key is missing.

Example:

```python
alien = {
    "color": "green",
}

points = alien.get("points")

print(points)
```

Output:

```text
None
```

`None` means “no value.”

Use a clear fallback message when you want readable output.

---

## Looping Through a Dictionary

You can loop through dictionaries in three main ways.

```text
.items()   key-value pairs
.keys()    keys only
.values()  values only
```

Choose the method based on what you need.

---

## Looping Through Key-Value Pairs with `.items()`

Use `.items()` when you need both the key and the value.

Example:

```python
user = {
    "username": "mcurie",
    "first_name": "marie",
    "last_name": "curie",
}

for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
```

The variable names can be more specific.

Example:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name, language in favorite_languages.items():
    print(f"{name.title()} likes {language.title()}.")
```

Use descriptive loop variable names when possible.

---

## Looping Through Keys with `.keys()`

Use `.keys()` when you only need the keys.

Example:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in favorite_languages.keys():
    print(name.title())
```

Looping directly over a dictionary also loops through its keys.

These two loops are equivalent:

```python
for name in favorite_languages.keys():
    print(name)

for name in favorite_languages:
    print(name)
```

Use `.keys()` when it makes your intention clearer.

---

## Checking Whether a Key Exists

Use `in` to check whether a key exists in a dictionary.

Example:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
}

if "erin" not in favorite_languages:
    print("Erin, please take the poll.")
```

This checks the dictionary keys.

You do not need to write `.keys()` for this check, but you can.

```python
if "erin" not in favorite_languages.keys():
    print("Erin, please take the poll.")
```

The shorter version is common:

```python
if "erin" not in favorite_languages:
    print("Erin, please take the poll.")
```

---

## Looping Through Keys in Sorted Order

Use `sorted()` when you want to loop through keys in alphabetical order.

Example:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

Important:

```text
sorted() returns a sorted list.
It does not permanently change the dictionary.
```

---

## Looping Through Values with `.values()`

Use `.values()` when you only need the values.

Example:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for language in favorite_languages.values():
    print(language.title())
```

This may show duplicate values.

Example:

```text
Python
C
Rust
Python
```

---

## Removing Duplicate Values with `set()`

Use `set()` when you want unique values.

Example:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for language in set(favorite_languages.values()):
    print(language.title())
```

A set stores unique items.

Example:

```python
languages = {"python", "rust", "python"}

print(languages)
```

The duplicate `"python"` is removed.

Do not rely on a set to keep items in a specific order.

---

## Nesting

Nesting means putting one data structure inside another.

Common Chapter 6 nesting patterns:

```text
- a list of dictionaries
- a list inside a dictionary
- a dictionary inside a dictionary
```

Nesting helps represent more complex data.

---

## A List of Dictionaries

Use a list of dictionaries when you have many similar objects.

Example:

```python
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

This is useful when each item has the same structure.

Examples:

```text
- many users
- many products
- many pets
- many game characters
```

---

## Creating Many Dictionaries with a Loop

You can create many dictionaries and append them to a list.

Example:

```python
aliens = []

for alien_number in range(30):
    new_alien = {
        "color": "green",
        "points": 5,
        "speed": "slow",
    }
    aliens.append(new_alien)

print(f"Total aliens: {len(aliens)}")
```

This combines:

```text
- an empty list
- a for loop
- a dictionary
- append()
- len()
```

---

## Modifying Dictionaries Inside a List

You can loop through a slice of a list and modify selected dictionaries.

Example:

```python
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
```

This changes only the first three aliens.

Important:

```text
aliens[:3] creates a slice of the first three dictionaries.
Each alien variable still refers to a dictionary object.
Changing the dictionary changes the object inside the original list.
```

---

## A List Inside a Dictionary

Use a list inside a dictionary when one key has multiple values.

Example:

```python
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

print(f"You ordered a {pizza['crust']}-crust pizza.")

for topping in pizza["toppings"]:
    print(f"Adding {topping}.")
```

The key `"toppings"` points to a list.

This is useful when one object has multiple related items.

Examples:

```text
- a pizza with many toppings
- a user with many roles
- a student with many grades
- a city with many landmarks
```

---

## Looping Through a List Inside a Dictionary

When a dictionary value is a list, use a nested loop.

Example:

```python
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
}

for name, languages in favorite_languages.items():
    print(f"{name.title()} likes:")

    for language in languages:
        print(f"- {language.title()}")
```

Outer loop:

```text
goes through each person
```

Inner loop:

```text
goes through that person's languages
```

---

## A Dictionary Inside a Dictionary

Use a dictionary inside a dictionary when each key points to a full record.

Example:

```python
users = {
    "aeinstein": {
        "first_name": "albert",
        "last_name": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first_name": "marie",
        "last_name": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info["location"]

    print(f"Username: {username}")
    print(f"Full name: {full_name.title()}")
    print(f"Location: {location.title()}")
```

This structure is useful when each record needs several fields.

Try to keep each inner dictionary with the same structure.

---

## When to Use Each Structure

```text
List:
Use when you have a sequence of items.

Dictionary:
Use when each value needs a label.

List of dictionaries:
Use when you have many similar records.

List inside a dictionary:
Use when one record has multiple values for one field.

Dictionary inside a dictionary:
Use when one lookup key points to a complete record.
```

---

## Common Mistakes

### Accessing a missing key with square brackets

Incorrect:

```python
alien = {"color": "green"}

print(alien["points"])
```

Correct:

```python
alien = {"color": "green"}

print(alien.get("points", "No points assigned."))
```

---

### Forgetting quotes around string keys

Incorrect:

```python
person = {
    first_name: "ada",
}
```

Correct:

```python
person = {
    "first_name": "ada",
}
```

---

### Mixing up keys and values

Incorrect:

```python
favorite_languages = {
    "jen": "python",
}

print(favorite_languages["python"])
```

Correct:

```python
favorite_languages = {
    "jen": "python",
}

print(favorite_languages["jen"])
```

`"jen"` is the key.

`"python"` is the value.

---

### Using `.items()` when only keys are needed

Works, but unnecessary:

```python
for name, language in favorite_languages.items():
    print(name)
```

Better:

```python
for name in favorite_languages:
    print(name)
```

---

### Using `.keys()` when checking membership is enough

Works, but longer:

```python
if "erin" not in favorite_languages.keys():
    print("Erin should take the poll.")
```

Better:

```python
if "erin" not in favorite_languages:
    print("Erin should take the poll.")
```

---

### Expecting `.values()` to remove duplicates

Incorrect assumption:

```python
for language in favorite_languages.values():
    print(language)
```

This can print duplicate values.

Use `set()` for unique values:

```python
for language in set(favorite_languages.values()):
    print(language)
```

---

### Nesting too deeply

Avoid structures that become hard to read.

Hard to understand:

```python
data = {
    "users": {
        "active": {
            "admins": [
                {"name": "ada", "permissions": ["read", "write", "delete"]}
            ]
        }
    }
}
```

Better:

```python
admins = [
    {
        "name": "ada",
        "permissions": ["read", "write", "delete"],
    }
]
```

Use helper variables when nesting becomes difficult to read.

---

### Confusing `return` and `print`

For exercises and tests, functions usually need to return values.

Less useful for testing:

```python
def get_points(alien):
    print(alien["points"])
```

Better:

```python
def get_points(alien):
    return alien["points"]
```

Use `print()` when displaying information to a human.

Use `return` when a function should give a value back to the program.

---

## Official Docs Practice

Chapter 6 connects to these Python documentation topics:

```text
Dictionaries
Dictionary methods
Sets
Built-in functions: sorted(), len()
```

### Official Reading Links

Read only these sections from the Python official documentation:

- [Dictionaries — Python Tutorial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Built-in Functions — sorted()](https://docs.python.org/3/library/functions.html#sorted)
- [Built-in Functions — len()](https://docs.python.org/3/library/functions.html#len)

When reading documentation, ask:

```text
1. What problem does this data structure or method solve?
2. What syntax does it use?
3. What does it return?
4. Does it mutate the dictionary or create a new value?
5. What happens if the key is missing?
6. Can I run one tiny example?
7. What mistake should I avoid?
```

### Small Experiments

```python
alien = {
    "color": "green",
    "points": 5,
}

print(alien["color"])
print(alien.get("speed", "No speed assigned."))

alien["speed"] = "slow"
print(alien)

alien["color"] = "yellow"
print(alien)

del alien["points"]
print(alien)

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

print(favorite_languages.keys())
print(favorite_languages.values())
print(favorite_languages.items())

print(sorted(favorite_languages.keys()))
print(set(favorite_languages.values()))
```

### Dictionaries

A dictionary maps keys to values.

#### Key takeaway

Your main rule should be:

```text
Use a dictionary when each value needs a meaningful label.
Use the key to retrieve the value.
Use .get() when the key might not exist.
```

### Dictionary Methods

Dictionary methods help you work with dictionary contents.

```text
.items()   returns key-value pairs
.keys()    returns keys
.values()  returns values
.get()     safely retrieves a value
```

#### Key takeaway

Choose the dictionary method based on what your loop needs.

```text
Need key and value? Use .items()
Need only keys? Loop over the dictionary or use .keys()
Need only values? Use .values()
Need safe access? Use .get()
```

### Sets

A set stores unique items.

Example:

```python
languages = ["python", "c", "python", "rust"]

unique_languages = set(languages)

print(unique_languages)
```

#### Key takeaway

Use `set()` when duplicates should be removed.

Do not use a set when order matters.

### `sorted()`

`sorted()` returns a new sorted list.

Example:

```python
names = ["sarah", "jen", "phil"]

sorted_names = sorted(names)

print(sorted_names)
print(names)
```

#### Key takeaway

`sorted()` does not permanently change the original collection.

---

## Key Corrections from Chapter 6

### Use `.get()` when a key might be missing

This is risky:

```python
points = alien["points"]
```

Use this when the key may not exist:

```python
points = alien.get("points", 0)
```

---

### Use `.items()` when you need both key and value

Less direct:

```python
for name in favorite_languages:
    language = favorite_languages[name]
    print(f"{name}: {language}")
```

More direct:

```python
for name, language in favorite_languages.items():
    print(f"{name}: {language}")
```

---

### Use `.values()` only when you do not need the keys

If you need the person and the language, do not use `.values()`.

Incorrect:

```python
for language in favorite_languages.values():
    print(f"{name} likes {language}")
```

Correct:

```python
for name, language in favorite_languages.items():
    print(f"{name} likes {language}")
```

---

### Keep nested structures readable

If a nested dictionary becomes difficult to read, split the logic into smaller variables.

Instead of reading everything directly inside an f-string:

```python
print(f"{users['mcurie']['first_name']} {users['mcurie']['last_name']}")
```

Use helper variables:

```python
user_info = users["mcurie"]
full_name = f"{user_info['first_name']} {user_info['last_name']}"

print(full_name.title())
```

---

### Be careful with f-string quotes

If the f-string uses double quotes outside, use single quotes for dictionary keys inside.

Correct:

```python
print(f"The alien is {alien['color']}.")
```

Also correct:

```python
print(f'The alien is {alien["color"]}.')
```

Incorrect:

```python
print(f"The alien is {alien["color"]}.")
```

---

## Code Review Checklist

When reviewing Chapter 6 code, check:

```text
- Did I use a dictionary when values need labels?
- Are the keys named clearly?
- Did I use quotes around string keys?
- Am I accessing the correct key?
- Should I use .get() instead of square brackets?
- Did I choose the correct loop method: .items(), .keys(), or .values()?
- Do I need sorted() for predictable output?
- Do I need set() to remove duplicates?
- Is my nested data structure still readable?
- Did I avoid nesting too deeply?
- Did I use return instead of print inside testable functions?
- Are f-string quotes correct when accessing dictionary values?
- Did I avoid repeated logic by using a loop or helper function?
```

---

## Review Questions

1. What is a dictionary?
2. What is a key-value pair?
3. How do you access a value by key?
4. What happens if you use square brackets with a missing key?
5. What does `.get()` do?
6. What does `.get()` return if the key is missing and no fallback is provided?
7. How do you add a new key-value pair?
8. How do you modify an existing value?
9. How do you delete a key-value pair?
10. What does `.items()` give you during a loop?
11. What does `.keys()` give you?
12. What does `.values()` give you?
13. Why might `.values()` print duplicates?
14. How does `set()` help with duplicate values?
15. What does `sorted()` do?
16. When should you use a list of dictionaries?
17. When should you put a list inside a dictionary?
18. When should you put a dictionary inside a dictionary?
19. Why should nested structures stay shallow when possible?
20. Why are dictionaries important for Django and web development?
