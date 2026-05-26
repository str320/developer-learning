from week_04_drills import (
    build_user_profile,
    get_user_city,
    count_favorite_languages,
    list_admin_users,
    move_pending_orders,
    remove_unavailable_item,
)

def test_build_user_profile():
    assert build_user_profile("sam", "doe", 32, "athens") == {
        "first_name": "sam",
        "last_name": "doe",
        "age": 32,
        "city": "athens",
    }

def test_get_user_city():
    assert get_user_city({"name": "sam", "city": "athens"}) == "athens"
    assert get_user_city({}) == "Unknown city"

def test_count_favorite_languages():
    favorite_languages = {
        "jen": "python",
        "sarah": "c",
        "edward": "python",
        "phil": "python",
        "erin": "java",
    }

    assert count_favorite_languages(favorite_languages) == {
        "python": 3,
        "c": 1,
        "java": 1,
    }

def test_list_admin_users():
    users = [
        {"username": "admin_user", "role": "admin"},
        {"username": "regular_user", "role": "member"},
        {"username": "moderator_user", "role": "admin"},
        {"username": "admin_user", "role": "admin"},
        {"role": "admin"},
        {"username": "regular_user", "role": "member"},
    ]
        
    assert list_admin_users(users) == ["admin_user", "moderator_user", "admin_user"]

def test_move_pending_orders():
    pending_orders = ["tuna", "veggie", "chicken"]

    assert move_pending_orders(pending_orders) ==  ["chicken", "veggie", "tuna"]

def test_remove_unavailable_item():
    items = ["pastrami", "tuna", "pastrami", "veggie", "pastrami"]
    unavailable_item = "pastrami"

    assert remove_unavailable_item(items, unavailable_item) == ["tuna", "veggie"]