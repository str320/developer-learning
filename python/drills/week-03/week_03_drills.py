# Drill 1 -- Is Even

def is_even(number):
    return number % 2 == 0

# Drill 2 -- Can Vote

def can_vote(age):
    return age >= 18

# Drill 3 -- Is Empty

def is_empty(items):
    return not (items)
    
# Drill 4 -- Has Admin Access

def has_admin_access(username):
    return username.lower() == "admin"
    
# Drill 5 -- Is Valid Username

def is_valid_username(username):
    return len(username) >= 3
     
# Drill 6 -- Is Adult

def is_adult(age):
    return age >= 18
    
# Drill 7 -- Is Positive

def is_positive(number):
    return number > 0
    
# Drill 8 -- Is Passing Grade

def is_passing_grade(grade):
    return grade >= 60

# Drill 9 -- Has Items

def has_items(items):
    return bool(items)
    
# Drill 10 -- Can Enter Club

def can_enter_club(age, has_id):
    return age >= 18 and has_id
    
# Drill 11 -- Is Discount Eligible

def is_discount_eligible(age):
    return age < 18 or age >= 65
    
# Drill 12 -- Is Available Username

def is_available_username(username, current_users):
    current_users_lower = [user.lower() for user in current_users]
    return username.lower() not in current_users_lower
    
# Challenge -- User Status

def user_status(username):
    if username.lower() == "admin":
        return "admin"
    elif not username:
        return "guest"
    else:
        return "user"
    
if __name__ == "__main__":
    assert is_even(4) is True
    assert is_even(5) is False

    assert can_vote(18) is True
    assert can_vote(17) is False

    assert is_empty([]) is True
    assert is_empty(["python"]) is False

    assert has_admin_access("admin") is True
    assert has_admin_access("strat") is False

    assert is_valid_username("ada") is True
    assert is_valid_username("ab") is False

    assert is_adult(21) is True
    assert is_adult(12) is False

    assert is_positive(5) is True
    assert is_positive(0) is False
    assert is_positive(-3) is False

    assert is_passing_grade(90) is True
    assert is_passing_grade(60) is True
    assert is_passing_grade(59) is False

    assert has_items([]) is False
    assert has_items(["python"]) is True

    assert can_enter_club(20, True) is True
    assert can_enter_club(20, False) is False
    assert can_enter_club(16, True) is False

    assert is_discount_eligible(16) is True
    assert is_discount_eligible(30) is False
    assert is_discount_eligible(70) is True

    assert is_available_username("Ada", ["admin", "ada", "eric"]) is False
    assert is_available_username("maria", ["admin", "ada", "eric"]) is True

    assert user_status("admin") == "admin"
    assert user_status("") == "guest"
    assert user_status("strat") == "user"

    print("All Week 3 drill tests passed.")