banned_users = ['andrew', 'carolina', 'david']
requested_toppings = ['mushrooms', 'onions', 'pineapple']
user = "marie"

# Checking Whether a Value Is in a List

if "mushrooms" in requested_toppings:
    print("True")
else:
    print("False")

# Checking Whether a Value Is Not in a List

if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish!")

