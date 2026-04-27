#Personal Message: Store a person's name in a variable, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

#Name Cases: Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.
name = "Eric"
print(name.title())
print(name.lower())
print(name.upper())

#Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
#Albert Einstein once said, "A person who never made a mistake never tried anything new."
quote = "A person who never made a mistake never tried anything new."
print(f'Albert Einstein once said, "{quote}"')

#Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person's name in a variable called famous_person. Then compose your message and store it in a new variable called message. Finally, print your message.
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "{quote}"'
print(message)

#stripping Names: Store a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name = " Eric "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

#File Extensions: Store a filename in a variable, and then use one of the string functions to make sure the filename ends with the extension .txt. If the filename doesn't end with .txt, add the extension to the end of the filename, and then print the filename.
file_name = "python_notes.txt"
print(file_name.removesuffix(".txt"))