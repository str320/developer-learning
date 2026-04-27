#Drill 1 — print() vs return

def show_greeting(name):
    print(f"Hello, {name}")

def make_greeting(name):
    return f"Hello, {name}"

show_greeting("Alice")
message = make_greeting("Bob")
print(message)

#Drill 2 — Simple Arithmetic Functions

def add_two(number):
    return number + 2

def double(number):
    return number * 2

def square(number):
    return number ** 2

print(add_two(4))
print(double(5))
print(square(3))

#Drill 3 — Constants

MINUTES_IN_HOUR = 60

def hours_to_minutes(hours):
    return hours * MINUTES_IN_HOUR

print(hours_to_minutes(2))
print(hours_to_minutes(1.5))

#Drill 4 — Lasagna-Style Practice
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2

def bake_time_remaining(minutes_in_oven):
    return EXPECTED_BAKE_TIME - minutes_in_oven

def preparation_time_in_minutes(number_of_layers):
    return  number_of_layers * PREPARATION_TIME_PER_LAYER
 
def elapsed_time_in_minutes(number_of_layers, minutes_in_oven):
    return  (number_of_layers * PREPARATION_TIME_PER_LAYER) + minutes_in_oven

print(bake_time_remaining(30), "min remaining")
print(preparation_time_in_minutes(3), "prep minutes")
print(elapsed_time_in_minutes(3, 20), "min passed")