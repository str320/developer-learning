from week_03_drills import (
    is_even,
    can_vote,
    is_empty,
    has_admin_access,
    is_valid_username,
    is_adult,
    is_positive,
    is_passing_grade,
    has_items,
    can_enter_club,
    is_discount_eligible,
    is_available_username,
    user_status,
)

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False

def test_can_vote():
    assert can_vote(18) is True
    assert can_vote(17) is False

def test_is_empty():
    assert is_empty([]) is True
    assert is_empty(["python"]) is False

def test_has_admin_access():
    assert has_admin_access("admin") is True
    assert has_admin_access("strat") is False

def test_is_valid_username():
    assert is_valid_username("ada") is True
    assert is_valid_username("ad") is False

def test_is_adult():
    assert is_adult(21) is True
    assert is_adult(12) is False

def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(0) is False
    assert is_positive(-3) is False

def test_is_passing_grade():
    assert is_passing_grade(90) is True
    assert is_passing_grade(60) is True
    assert is_passing_grade(59) is False

def test_has_items():
    assert has_items([]) is False
    assert has_items(["python"]) is True

def test_can_enter_club():
    assert can_enter_club(20, True) is True
    assert can_enter_club(20, False) is False
    assert can_enter_club(16, True) is False

def test_is_discount_eligible():
    assert is_discount_eligible(16) is True
    assert is_discount_eligible(30) is False
    assert is_discount_eligible(70) is True
    assert is_discount_eligible(65) is True

def test_is_available_username():
    assert is_available_username("Ada", ["admin", "ada", "eric"]) is False
    assert is_available_username("maria", ["admin", "ada", "eric"]) is True
    assert is_available_username("ada", ["Admin", "Ada", "Eric"]) is False


def test_user_status():
    assert user_status("admin") == "admin"
    assert user_status("") == "guest"
    assert user_status("strat") == "user"