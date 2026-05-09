usernames = ["admin", "jaden", "ada", "eric", "guido"]
usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print(f"Hello super{username}")
        else:
            print(f"Hello user {username}")
else:
    print("We need to find some users!")
