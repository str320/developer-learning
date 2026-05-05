from week_02_drills import (
    first_item,
    last_item,
    total_numbers,
    biggest_number,
    smallest_number,
    double_numbers,
    doubled_numbers,
    square_numbers,
    long_words,
    longer_words,
    first_three,
    last_three,
    copy_and_add,
    menu_items,
    digit_powers
)

def test_first_item():
    assert first_item(["python", "django", "react"]) == "python"

def test_last_item():
    assert last_item(["python", "django", "react"]) == "react"

def test_total_numbers():
    assert total_numbers([1, 2, 3, 4, 5]) == 15

def test_biggest_number():
    assert biggest_number([3, 9, 2, 12, 5]) == 12

def test_smallest_number():
    assert smallest_number([3, 9, 2, 12, 5]) == 2

def test_double_numbers():
    assert double_numbers([1, 2, 3, 4]) == [2, 4, 6, 8]

def test_doubled_numbers():
    assert doubled_numbers([1, 2, 3, 4]) == [2, 4, 6, 8]

def test_square_numbers():
    assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]

def test_long_words():
    assert long_words(["python", "js", "django", "react", "postgres"]) == ['python', 'django', 'postgres']

def test_longer_words():
    assert longer_words(["python", "js", "django", "react", "postgres"]) == ['python', 'django', 'postgres']

def test_first_three():
    assert first_three(["a", "b", "c", "d", "e"]) == ['a', 'b', 'c']

def test_last_three():
    assert last_three(["a", "b", "c", "d", "e"]) == ['c', 'd', 'e']

def test_copy_and_add():
    assert copy_and_add(["pizza", "falafel", "carrot cake"], "cannoli") == ['pizza', 'falafel', 'carrot cake', 'cannoli']

def test_menu_items():
    assert menu_items(("rice", "beans", "salad")) == ['Rice', 'Beans', 'Salad']

def test_digit_powers():
    assert digit_powers(153) == [1, 125, 27]