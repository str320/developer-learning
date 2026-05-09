current_users = ["admin", "jaden", "ada", "eric", "guido"]
new_users = ["sarah", "ERIC", "maria", "Admin", "linus"]

current_users_lower = [user.lower() for user in current_users]

for username in new_users:
    if username.lower() in current_users_lower:
        print(f"This username [{username}] already exists, please enter a new username!")
    else:
        print(f"The username [{username}] is available!")