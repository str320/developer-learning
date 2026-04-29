from week_01_drills import (
    add_two,
    double,
    square,
    hours_to_minutes,
    bake_time_remaining,
    preparation_time_in_minutes,
    elapsed_time_in_minutes,
    introduce,
    age_message,
    add_string_numbers,
    exchange_money,
    get_change,
    multiply_by_three,
    minutes_to_seconds,
    days_to_hours,
    total_study_minutes,
    completed_lesson_message,
    )

assert add_two(5) == 7
assert double(6) == 12
assert square(4) == 16

assert hours_to_minutes(2) == 120
assert bake_time_remaining(30) == 10
assert preparation_time_in_minutes(3) == 6
assert elapsed_time_in_minutes(3, 20) == 26

assert introduce("Strat", "Python") == "Hi, I am Strat and I am learning Python."
assert age_message("Ada", 36) == "Ada is 36 years old."
assert add_string_numbers("10", "5") == 15

assert exchange_money(100, 1.25) == 80.0
assert get_change(100, 40) == 60

assert multiply_by_three(4) == 12
assert minutes_to_seconds(3) == 180
assert days_to_hours(2) == 48
assert total_study_minutes(2, 30) == 150
assert completed_lesson_message("Ch. 1") == "Completed: Ch. 1"