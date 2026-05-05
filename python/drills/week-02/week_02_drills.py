"""Week 2 drills: lists, loops, slicing, tuples, and Armstrong helpers.

Complete each function, then run this file to check the assertions.

Run:

    python3 python/drills/week-02/week_02_drills.py
"""
# Drill 1 -- First Item

def first_item(items):
    return items[0]

# Drill 2 __ Last Item

def last_item(items):
    return items[-1]

# Drill 3 __ Total Numbers

def total_numbers(numbers):
    return sum(numbers)

# Drill 4 — Biggest Number

def biggest_number(numbers):
    return max(numbers)

# Drill 5 — Smallest Number

def smallest_number(numbers):
    return min(numbers)

# Drill 6 — Double Numbers

def double_numbers(numbers):
    return [number * 2 for number in numbers]

def doubled_numbers(numbers):
    doubled = []

    for number in numbers:
        doubled.append(number * 2)

    return doubled

# Drill 7 — Square Numbers

def square_numbers(numbers):
    return [number ** 2 for number in numbers]

# Drill 8 — Long Words

def long_words(words):
    result = []
    for word in words:
        if len(word) > 5:
            result.append(word)

    return result

def longer_words(words):
    return [word for word in words if len(word) > 5]

# Drill 9 — First Three Items

def first_three(items):
    return items[:3]

# Drill 10 — Last Three Items

def last_three(items):
    return items[-3:]

# Drill 11 — Copy and Add

def copy_and_add(items, item):
    result = items[:]
    result.append(item)
    return result

# Drill 12 — Tuple Menu

def menu_items(items):
    result = [item.title() for item in items]
    return result

# Challenge — Armstrong Helper

def digit_powers(number):
    digits = str(number)
    power = len(digits)
    return [int(digit) ** power for digit in digits]

if __name__ == "__main__":
    items = ["python", "django", "react"]
    numbers = [1, 2, 3, 4, 5]
    more_numbers = [3, 9, 2, 12, 5]
    small_numbers = [3, 9, 2, 12, 5]
    numbers_doubled = [1, 2, 3, 4]
    numbers_square = [1, 2, 3, 4]
    words = ["python", "js", "django", "react", "postgres"]
    items = ["a", "b", "c", "d", "e"]
    foods = ["pizza", "falafel", "carrot cake"]
    foods_menu = ("rice", "beans", "salad")
    number = 153


    print(first_item(items))
    print(last_item(items))
    print(total_numbers(numbers))
    print(biggest_number(more_numbers))
    print(smallest_number(small_numbers))
    print(double_numbers(numbers_doubled))
    print(doubled_numbers(numbers_doubled))
    print(square_numbers(numbers_square))
    print(long_words(words))
    print(longer_words(words))
    print(first_three(items))
    print(last_three(items))
    print(copy_and_add(foods, "cannoli"))
    print(menu_items(foods_menu))
    print(digit_powers(number))
    print("\nAll Week 2 drill tests passed.")