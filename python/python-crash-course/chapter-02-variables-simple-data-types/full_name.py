# This program demonstrates how to use variables and string formatting to create a full name and greet the user.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# Another way to do it
message = f"Hello, {full_name.title()}!"
print(message)

# Stripping whitespace from a string
favorite_language = "python "
favorite_language = favorite_language.rstrip()
print(favorite_language)

# Removing a prefix from a string
nostarch_url = "https://nostarch.com"
nostarch_url.removeprefix("https://")
print(nostarch_url)


