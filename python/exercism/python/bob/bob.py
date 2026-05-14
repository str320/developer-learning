def response(hey_bob):
    message = hey_bob.strip()

    is_silence = message == ""
    is_yelling = message.isupper()
    is_question = message.endswith("?")

    if is_silence:
        return "Fine. Be that way!"
    
    elif is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    elif is_yelling:
        return "Whoa, chill out!"
    
    elif is_question:
        return "Sure."
    
    return "Whatever."
