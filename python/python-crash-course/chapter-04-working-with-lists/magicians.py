magicians = ['alice', 'david', 'carolina']

#Looping Through an Entire List
for magician in magicians:
    print(magician)

# Every indented line following the line for magician in magicians is considered inside the loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!\n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.upper()}.\n")

#Doing Something After a for Loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can wait to see your next trick, {magician.upper()}.\n")
print(f"Thank you, everyone. That was a great magic show!")