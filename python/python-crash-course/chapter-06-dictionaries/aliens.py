# A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.

aliens_0 = []

for number_alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens_0.append(new_alien)

# Show the first 5 aliens

for alien in aliens[:5]:
    print(alien)


print(f"Total number of aliens: {len(aliens_0)}")

for alien in aliens_0[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens_0[:5]:
    print(alien)

