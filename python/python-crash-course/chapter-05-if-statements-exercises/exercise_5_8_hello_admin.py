usernames = ["admin", "jaden", "ada", "eric", "guido"]

for user in usernames:
    if user == "admin":
        print(f"Hello superuser [ {user.upper()} ]")
    else:
        print(f"\nHello user {user.title()}")