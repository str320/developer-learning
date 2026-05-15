def translate_word(word):
    vowels = ["a", "e", "i", "o","u"]
    special_starts = ["xr", "yt"]

    first_letter = word[0]
    first_two_letters = word[:2]

    starts_with_vowel = first_letter in vowels
    starts_with_special_sound = first_two_letters in special_starts

    if starts_with_vowel or starts_with_special_sound:
        return f"{word}ay"
    
    for index, letter in enumerate(word):
            if letter == "q" and word[index + 1] == "u":
                split_point = index + 2
                prefix = word[:split_point]
                rest = word[split_point:]
                return f"{rest}{prefix}ay"
            
            elif letter == "y" and index > 0:
                 prefix = word[:index]
                 rest = word[index:]
                 return f"{rest}{prefix}ay"
    
            if letter in vowels:
                prefix = word[:index]
                rest = word[index:]
                return f"{rest}{prefix}ay"
        

def translate(text):
    words = text.split()
    result = [translate_word(word) for word in words]
    return " ".join(result)






