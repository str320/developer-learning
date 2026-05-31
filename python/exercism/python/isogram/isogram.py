def is_isogram(string):
    lowercase_char = []

    for char in string:
        lowercased = char.lower()

        if lowercased == " " or lowercased == "-":
            continue
        
        if lowercased in lowercase_char:
            return False
        
        lowercase_char.append(lowercased)
    
    return True