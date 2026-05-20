# Exercise 6-4 — Glossary 2

glossary = {
    "variable": "A name that refers to a value.",
    "list": "An ordered collection of values.",
    "loop": "A way to repeat code.",
    "string": "Text data surrounded by quotes.",
    "boolean": "A value that is either True or False.",
    "dictionary": "A collection of key-value pairs.",
    "key": "A label used to access a value in a dictionary.",
    "value": "Data stored under a key.",
    "method": "A function attached to an object.",
    "condition": "An expression that evaluates to True or False.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}: \n{meaning}\n")

    