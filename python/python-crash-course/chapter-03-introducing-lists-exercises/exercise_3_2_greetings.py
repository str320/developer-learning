from exercise_3_1_names import (names)
message_1 = f"Hello, {names[0].title()} nice to meet you."
message_2 = f"Hello, {names[1].upper()} you have a nice bicycle."
message_3 = f"Hello, {names[2].lower()} waiting for you to call me."
message_4 = f"Hello, {names[3].title()} let's go for dinner tonight."
message_5 = f"Hello, {names[4].title()} we go for climbing next week."
message_6 = f"Hello, {names[-1].title()} great to hear back from you."

if __name__ == "__main__":
    print(message_1)
    print(message_2)
    print(message_3)
    print(message_4)
    print(message_5)
    print(message_6)