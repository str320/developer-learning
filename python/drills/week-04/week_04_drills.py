# Drill 1 — Build a User Profile Dictionary

def build_user_profile(first_name, last_name, age, city):
    user_profile = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "city": city
    }

    return user_profile

# Drill 2 — Get a City Safely with .get()

def get_user_city(user):
    return user.get("city", "Unknown city")

# Drill 3 — Count Favorite Languages

def count_favorite_languages(favorite_languages):
    new_dictionary = {}

    for current_language in favorite_languages.values():
        new_dictionary[current_language] = new_dictionary.get(current_language, 0) + 1

    return new_dictionary

# Drill 4 — List Admin Users

def list_admin_users(users):

    admin_users = []

    for user in users:
        if user.get("role", "") == "admin":
            username = user.get("username")
            if username:
                admin_users.append(username)
    
    return admin_users

# Drill 5 — Move Pending Orders

def move_pending_orders(pending_orders):
    finished_orders = []

    while pending_orders:
        current_order = pending_orders.pop()
        finished_orders.append(current_order)

    return finished_orders

# Drill 6 — Remove an Unavailable Item

def remove_unavailable_item(items, unavailable_item):

    while unavailable_item in items:
        items.remove(unavailable_item)

    return items

if __name__ == "__main__":
    favorite_languages = {
        "jen": "python",
        "sarah": "c",
        "edward": "python",
        "phil": "python",
        "erin": "java",
    }
    
    users = [
        {"username": "regular_user", "role": "member"},
        {"username": "moderator_user", "role": "admin"},
        {"username": "admin_user", "role": "admin"},
        {"role": "admin"},
        {"username": "regular_user", "role": "member"}
    ]

    pending_orders = ["tuna", "veggie", "chicken"]

    items = ["pastrami", "tuna", "pastrami", "veggie", "pastrami"]
    unavailable_item = "pastrami"
    
    print(build_user_profile("sam", "doe", 32, "athens"))
    print(get_user_city({"name": "sam", "city": "athens"}))
    print(get_user_city({}))
    print(count_favorite_languages(favorite_languages))
    print(list_admin_users(users))
    print(move_pending_orders(pending_orders))
    print(remove_unavailable_item(items, unavailable_item))