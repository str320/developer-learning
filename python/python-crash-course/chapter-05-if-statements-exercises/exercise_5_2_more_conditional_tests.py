language = "Python"
age = 21
favorite_languages = ["python", "javascript", "sql"]

# 1
print("language != 'python' : True")
print(language != "python")

print("\nlanguage == 'python' : False")
print(language == "python")

# 2
print("\nlanguage.lower() == 'python' : True")
print(language.lower() == "python")

print("\nlanguage.lower() != 'python' : False")
print(language.lower() != 'python')

# 3
print("\nage == 21 : True")
print(age == 21)

print("\nage != 21 : False")
print(age != 21)

print("\nage > 18 : True")
print(age > 18)

print("\nage < 18 : False")
print(age < 18)

print("\nage >= 21 : True")
print(age >= 21)

print("\nage <= 18 : False")
print(age <= 18)

# 4
print("\nlanguage != 'python' and age == 21 : True")
print(language != "python" and age == 21)

print("\nlanguage == 'python' and age != 21 : False")
print(language == "python" and age != 21)

# 5 
print("\nlanguage == 'python' or age == 21 : True")
print(language == 'python' or age == 21)

print("\nlanguage == 'python' or age != 21 : False")
print(language == 'python' or age != 21)

# 6
print("\npython in favorite_languages : True")
print('python' in favorite_languages)

# 7
print("\nlanguage not in favorite_languages : False")
print(language.lower() not in favorite_languages)
