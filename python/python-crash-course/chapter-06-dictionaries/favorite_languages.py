favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages["edward"].title()
print(language)

# Using get() to Access Values

language_1 = favorite_languages.get("jen", "No name value assigned").title()
print(language_1)

language_2 = favorite_languages.get("stratos", "No name value assigned").title()
print(language_2)

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    
    for language in languages:
        print(f"\t{language.title()}")
