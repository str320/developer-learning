# Chapter 3 Notes — Introducing Lists

These notes summarize the most important ideas from **Python Crash Course Chapter 3: Introducing Lists**.

---

## What Chapter 3 Is About

Chapter 3 introduces lists.

A list lets you store multiple values in one variable.

You learned how to:

```text
- create lists
- access list items
- use indexes
- use negative indexes
- modify list items
- add items
- remove items
- sort lists
- find list length
```

---

## Lists

A list is an ordered collection of values.

Example:

```python
names = ["ada", "eric", "guido"]
```

Lists use square brackets:

```python
[]
```

Items are separated with commas.

---

## Accessing Items

Python indexes start at `0`.

Example:

```python
names = ["ada", "eric", "guido"]

print(names[0])
print(names[1])
print(names[2])
```

Output:

```text
ada
eric
guido
```

Index positions:

```text
0 → ada
1 → eric
2 → guido
```

---

## Negative Indexes

Negative indexes count from the end of the list.

Example:

```python
names = ["ada", "eric", "guido"]

print(names[-1])
print(names[-2])
```

Output:

```text
guido
eric
```

Use `[-1]` when you want the last item.

---

## Using List Items in Messages

You can use a list item inside an f-string.

Example:

```python
names = ["ada", "eric", "guido"]

print(f"Hello, {names[0].title()}!")
```

Output:

```text
Hello, Ada!
```

---

## Modifying Items

Lists are mutable, which means you can change their items.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[0] = "ducati"

print(motorcycles)
```

Output:

```text
["ducati", "yamaha", "suzuki"]
```

---

## Adding Items with `.append()`

`.append()` adds one item to the end of a list.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append("ducati")

print(motorcycles)
```

Output:

```text
["honda", "yamaha", "suzuki", "ducati"]
```

Important:

```text
append() mutates the original list and returns None.
```

---

## Inserting Items with `.insert()`

`.insert()` adds an item at a specific position.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")

print(motorcycles)
```

Output:

```text
["ducati", "honda", "yamaha", "suzuki"]
```

The first argument is the index.

The second argument is the item to insert.

---

## Removing Items with `del`

Use `del` when you know the index of the item you want to remove.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[0]

print(motorcycles)
```

Output:

```text
["yamaha", "suzuki"]
```

`del` removes the item permanently.

---

## Removing Items with `.pop()`

`.pop()` removes and returns an item.

By default, it removes the last item.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
popped_motorcycle = motorcycles.pop()

print(popped_motorcycle)
print(motorcycles)
```

Output:

```text
suzuki
["honda", "yamaha"]
```

Use `.pop()` when you want to remove an item but still use it.

You can also pop by index:

```python
first_owned = motorcycles.pop(0)
```

---

## Removing by Value with `.remove()`

`.remove()` removes the first matching value.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.remove("yamaha")

print(motorcycles)
```

Output:

```text
["honda", "suzuki"]
```

Use `.remove()` when you know the value but not the index.

Important:

```text
remove() only removes the first matching value.
```

---

## Sorting Permanently with `.sort()`

`.sort()` changes the original list.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()

print(cars)
```

Output:

```text
["audi", "bmw", "subaru", "toyota"]
```

Reverse order:

```python
cars.sort(reverse=True)
```

Important:

```text
sort() mutates the original list and returns None.
```

---

## Sorting Temporarily with `sorted()`

`sorted()` returns a sorted copy and keeps the original list unchanged.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]

print(sorted(cars))
print(cars)
```

Use `sorted()` when you want to display a sorted version without changing the original.

---

## Reversing a List

`.reverse()` reverses the original list order.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()

print(cars)
```

Important:

```text
reverse() mutates the original list.
```

It does not sort alphabetically; it only reverses the current order.

---

## List Length with `len()`

`len()` returns how many items are in a list.

Example:

```python
guests = ["ada", "eric", "guido"]

print(len(guests))
```

Output:

```text
3
```

---

## Common Mistakes

### Forgetting indexes start at 0

Incorrect:

```python
names = ["ada", "eric", "guido"]
print(names[3])
```

This raises an `IndexError`.

Correct:

```python
print(names[2])
```

### Confusing `.sort()` and `sorted()`

```python
cars.sort()     # changes original list
sorted(cars)    # returns sorted copy
```

### Expecting `.append()` to return a new list

Incorrect:

```python
names = ["ada", "eric"]
result = names.append("guido")

print(result)  # None
```

Correct:

```python
names.append("guido")
print(names)
```

---

## Key Corrections from Chapter 3

### Mutation matters

Some methods change the original list:

```text
append()
insert()
remove()
pop()
sort()
reverse()
```

Some functions return a new value:

```text
sorted()
len()
```

### Choose removal tools intentionally

Use:

```text
del        when you know the index and do not need the item
pop()      when you want to remove and use the item
remove()   when you know the value
```

---

## Review Questions

1. What is a list?
- A list is an ordered collection of values stored in one variable.
- Lists use square brackets, and items are separated by commas.

Example:

```python
names = ["ada", "eric", "guido"]
```

2. What index does Python start counting from?
- Python starts counting list indexes from `0`.

Example:

```python
names = ["ada", "eric", "guido"]

print(names[0])
# ada
```

3. What does `names[-1]` return?
- `names[-1]` returns the last item in the list.

Example:

```python
names = ["ada", "eric", "guido"]

print(names[-1])
# guido
```

4. How do you modify an item in a list?
- Assign a new value to a specific index.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[0] = "ducati"

print(motorcycles)
# ["ducati", "yamaha", "suzuki"]
```

5. What does `.append()` do?
- `.append()` adds one item to the end of a list.
- It mutates the original list and returns `None`.

Example:

```python
motorcycles = ["honda", "yamaha"]
motorcycles.append("suzuki")

print(motorcycles)
# ["honda", "yamaha", "suzuki"]
```

6. What does `.insert()` do?
- `.insert()` adds an item at a specific index.
- The first argument is the index.
- The second argument is the value to insert.

Example:

```python
motorcycles = ["honda", "yamaha"]
motorcycles.insert(0, "ducati")

print(motorcycles)
# ["ducati", "honda", "yamaha"]
```

7. When should you use `del`?
- Use `del` when you know the index of the item you want to remove and you do not need to use the removed value.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[0]

print(motorcycles)
# ["yamaha", "suzuki"]
```

8. When should you use `.pop()`?
- Use `.pop()` when you want to remove an item and still use the removed value.
- Without an index, `.pop()` removes and returns the last item.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
popped_motorcycle = motorcycles.pop()

print(popped_motorcycle)
# suzuki
```

9. When should you use `.remove()`?
- Use `.remove()` when you know the value you want to remove, not the index.
- `.remove()` removes only the first matching value.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.remove("yamaha")

print(motorcycles)
# ["honda", "suzuki"]
```

10. What is the difference between `.sort()` and `sorted()`?
- `.sort()` permanently changes the original list and returns `None`.
- `sorted()` returns a sorted copy and keeps the original list unchanged.

Example:

```python
cars = ["bmw", "audi", "toyota"]

print(sorted(cars))
print(cars)

cars.sort()
print(cars)
```

11. What does `.reverse()` do?
- `.reverse()` reverses the current order of the original list.
- It mutates the list.
- It does not sort alphabetically.

Example:

```python
cars = ["bmw", "audi", "toyota"]
cars.reverse()

print(cars)
# ["toyota", "audi", "bmw"]
```

12. What does `len()` return?
- `len()` returns the number of items in a list.

Example:

```python
guests = ["ada", "eric", "guido"]

print(len(guests))
# 3
```

13. Which list methods mutate the original list?
- These common list methods mutate the original list:

```text
append()
insert()
remove()
pop()
sort()
reverse()
```

- These return useful values without changing the original list, depending on the operation:

```text
sorted()
len()
```
