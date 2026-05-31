def rotate(text, key):
    # Create lowercase and uppercase alphabets
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Normalize the key
    key %= 26

    #Create an empty result list
    result = []

    # Loop through each character
    for ch in text:
        # If lowercase, rotate inside lowercase alphabet
        if ch.islower():

            # This finds the position of the lowercase character inside the lowercase alphabet
            idx = lowercase.index(ch)

            # This is the main rotation logic, moves the letter forward
            # The % 26 handles wrapping
            # Adds the rotated letter to your result list
            result.append(lowercase[(idx + key) % 26])

        # This runs only if the first condition was false
        # If uppercase, rotate inside uppercase alphabet
        elif ch.isupper():

            # This finds the uppercase character’s position in the uppercase alphabet
            idx = uppercase.index(ch)

            # This is the main rotation logic, moves the letter forward
            # The % 26 handles wrapping
            # Adds the rotated letter to your result list
            result.append(uppercase[(idx + key) % 26])

        # Otherwise, keep the character unchanged
        else:
            result.append(ch)
    # Otherwise, keep the character unchanged
    return "".join(result)