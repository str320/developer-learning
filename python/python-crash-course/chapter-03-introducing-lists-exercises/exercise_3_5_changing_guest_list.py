guests = ["Ada Lovelace", "Alan Turing", "Grace Hopper"]

if __name__ == "__main__":
    print(f"{guests[1]}, can't make it to dinner.")
    guests[1] = "John Alan"

    print(f"\n{guests[0]}, I would like to invite you for dinner tonight.")
    print(f"\n{guests[1]}, I would like to invite you for dinner tonight.")
    print(f"\n{guests[2]}, I would like to invite you for dinner tonight.")