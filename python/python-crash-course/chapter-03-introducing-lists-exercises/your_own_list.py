motorcycles = ["Yamaha", "Honda", "Kawasaki", "Ducati", "Suzuki", "BMW"]

message_1 = f"I would like to own a {motorcycles[0].title()} motorcycle."
message_2 = f"I had a {motorcycles[1].title()} motorcycle back in the day."
message_3 = f"I never had a {motorcycles[2].title()} motorcycle."
message_4 = f"{motorcycles[3].title()} motorcycle is my dream bike."
message_5 = f"{motorcycles[4].title()} motorcycles they have really nice dirt bikes."
message_6 = f"I am not a fan of {motorcycles[-1].title()} motorcycles."

if __name__ == "__main__":
    print(message_1)
    print(message_2)
    print(message_3)
    print(message_4)
    print(message_5)
    print(message_6)