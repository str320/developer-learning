#Drill 1 — print() vs return

def show_greeting(name):
    print(f"Hello, {name}!")

def make_greeting(name):
    return f"Hello, {name}!"

#Drill 2 — Simple Arithmetic Functions

def add_two(number):
    return number + 2

def double(number):
    return number * 2

def square(number):
    return number ** 2

#Drill 3 — Constants

MINUTES_IN_HOUR = 60
def hours_to_minutes(hours):
    return hours * MINUTES_IN_HOUR

#Drill 4 — Lasagna-Style Practice

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2

def bake_time_remaining(minutes_in_oven):
    return EXPECTED_BAKE_TIME - minutes_in_oven

def preparation_time_in_minutes(number_of_layers):
    return  number_of_layers * PREPARATION_TIME_PER_LAYER
 
def elapsed_time_in_minutes(number_of_layers, minutes_in_oven):
    return  (number_of_layers * PREPARATION_TIME_PER_LAYER) + minutes_in_oven

#Drill 5 — Strings and f-strings

def introduce(name, language):
    return f"Hi, I am {name} and I am learning {language}."

#Drill 6 — Type Conversion

def age_message(name, age):
    return f"{name} is {age} years old"

def add_string_numbers(first, second):
    return int(first) + int(second)

#Drill 7 — Currency-Style Practice

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchange_value):
    return budget - exchange_value

#Drill 8 — Debugging Syntax Mistakes
# Broken version:

#def favorite_language(name, language)
#   return f"{name} like {language}"

# Error:
# SyntaxError: expected ':'
# The first line is wrong.
# The missing character is ':'.
# Python uses the colon to mark the start of an indented code block.

# Drill 9 — Indentation Practice

def multiply_by_three(number):
    return number * 3

#Drill 10 — Mini Review Function Set

def minutes_to_seconds(minutes):
    return minutes * 60

def days_to_hours(days):
    return days * 24

def total_study_minutes(hours, minutes):
    return (hours * 60) + minutes

def completed_lesson_message(lesson_name):
    return f"Completed: {lesson_name}"

if __name__ == "__main__":
    print("\n\tDrill 1\n")
    show_greeting("Alice")
    message = make_greeting("Bob")
    print(message)

    print("\n\tDrill 2\n")
    print(add_two(4))
    print(double(5))
    print(square(3))

    print("\n\tDrill 3\n")
    print(hours_to_minutes(2))
    print(hours_to_minutes(1.5))

    print("\n\tDrill 4\n")
    print(bake_time_remaining(30), "min remaining")
    print(preparation_time_in_minutes(3), "prep minutes")
    print(elapsed_time_in_minutes(3, 20), "min passed")

    print("\n\tDrill 5\n")
    print(introduce("Strat", "Python"))

    print("\n\tDrill 6\n")
    print(age_message("Ada", 36))
    print(add_string_numbers("10", "5"))

    print("\n\tDrill 7\n")
    print(exchange_money(100, 1.25))
    print(get_change(100, 40))

    print("\n\tDrill 8\n")
    print("SyntaxError: expected ':'")

    print("\n\tDrill 9\n")
    print(multiply_by_three(4))

    print("\n\tDrill 10\n")
    print(minutes_to_seconds(3))
    print(days_to_hours(2))
    print(total_study_minutes(2, 30))
    print(completed_lesson_message("Ch. 1"))