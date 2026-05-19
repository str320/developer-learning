# A Simple Dictionary

alien_0 = {'color': 'green', 'points': 5}
print(alien_0["color"])
print(alien_0["points"])

# Accessing Values in a Dictionary

print(alien_0["color"])

# Adding New Key-Value Pairs

alien_0["x_position"] = 0
print(alien_0)

alien_0["y_position"] = 25
print(alien_0)

# Starting with an Empty Dictionary

alien_1 = {}
print(alien_1)

# Modifying Values in a Dictionary

print(f"The alien is {alien_0["color"]}")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}")

alien_0["speed"] = "medium"
print(alien_0)

print(f"Original position: {alien_0["x_position"]}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

if alien_0["speed"] == "slow":
    x_increment = 1

elif alien_0["speed"] == "medium":
    x_increment = 2
    
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0["points"]
print(alien_0)