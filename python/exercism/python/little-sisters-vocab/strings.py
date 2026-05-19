"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return f"un{word}"

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words."""
    prefix = vocab_words[0]
    prefixed_words = [f"{prefix}{word}" for word in vocab_words[1:]]
    result = [prefix] + prefixed_words
    
    return " :: ".join(result)

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""

    root = word[:-4]

    if root.endswith("i"):
        return f"{root[:-1]}y"

    return root

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""

    words = sentence.split()
    adjective = words[index].removesuffix(".")

    return f"{adjective}en"