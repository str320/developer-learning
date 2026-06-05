def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    seen_letters = set()

    for ch in sentence:
        if ch == " " or ch == "-":
            continue

        if ch.lower() in alphabet:
            seen_letters.add(ch.lower())

    return len(seen_letters) == len(alphabet)