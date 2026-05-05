"""Week 2 drills: lists, loops, slicing, tuples, and Armstrong helpers.

Complete each function, then run this file to check the assertions.

Run:

    python3 python/drills/week-02/week_02_drills.py
"""


def first_item(items):
    """Return the first item in a list."""
    # TODO: return the item at index 0
    pass


def last_item(items):
    """Return the last item in a list."""
    # TODO: return the item at index -1
    pass


def total_numbers(numbers):
    """Return the total of a list of numbers."""
    # TODO: return the sum of the numbers
    pass


def biggest_number(numbers):
    """Return the largest number in a list."""
    # TODO: return the largest number
    pass


def smallest_number(numbers):
    """Return the smallest number in a list."""
    # TODO: return the smallest number
    pass


def double_numbers(numbers):
    """Return a new list where every number is doubled."""
    # TODO:
    # 1. create an empty list
    # 2. loop through numbers
    # 3. append number * 2
    # 4. return the new list
    pass


def square_numbers(numbers):
    """Return a new list where every number is squared."""
    # TODO:
    # 1. create an empty list
    # 2. loop through numbers
    # 3. append number ** 2
    # 4. return the new list
    pass


def long_words(words):
    """Return words longer than 5 characters."""
    # TODO:
    # 1. create an empty list
    # 2. loop through words
    # 3. if len(word) > 5, append it
    # 4. return the new list
    pass


def first_three(items):
    """Return the first three items from a list."""
    # TODO: return a slice of the first three items
    pass


def last_three(items):
    """Return the last three items from a list."""
    # TODO: return a slice of the last three items
    pass


def copy_and_add(items, new_item):
    """Return a copied list with a new item added.

    The original list should not change.
    """
    # TODO:
    # 1. copy the list using slicing
    # 2. append the new item to the copy
    # 3. return the copy
    pass


def menu_items(foods):
    """Return a list of title-cased food names from a tuple."""
    # TODO:
    # 1. create an empty list
    # 2. loop through the tuple
    # 3. append food.title()
    # 4. return the new list
    pass


def digit_powers(number):
    """Return each digit raised to the power of the number of digits.

    Example:
        153 -> [1, 125, 27]
    """
    # TODO:
    # 1. convert number to a string
    # 2. calculate the power using len()
    # 3. loop through each digit
    # 4. convert digit back to int
    # 5. append int(digit) ** power
    # 6. return the list
    pass


if __name__ == "__main__":
    assert first_item(["python", "django", "react"]) == "python"
    assert last_item(["python", "django", "react"]) == "react"
    assert total_numbers([1, 2, 3, 4, 5]) == 15
    assert biggest_number([3, 9, 2, 12, 5]) == 12
    assert smallest_number([3, 9, 2, 12, 5]) == 2
    assert double_numbers([1, 2, 3, 4]) == [2, 4, 6, 8]
    assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert long_words(["python", "js", "django", "react", "postgres"]) == [
        "python",
        "django",
        "postgres",
    ]
    assert first_three(["a", "b", "c", "d", "e"]) == ["a", "b", "c"]
    assert last_three(["a", "b", "c", "d", "e"]) == ["c", "d", "e"]

    foods = ["pizza", "falafel", "carrot cake"]
    copied_foods = copy_and_add(foods, "cannoli")

    assert copied_foods == ["pizza", "falafel", "carrot cake", "cannoli"]
    assert foods == ["pizza", "falafel", "carrot cake"]

    assert menu_items(("rice", "beans", "salad")) == ["Rice", "Beans", "Salad"]
    assert digit_powers(153) == [1, 125, 27]
    assert digit_powers(9) == [9]

    print("All Week 2 drill tests passed.")
