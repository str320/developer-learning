def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number - 1)


def total():
    total_grains = 0

    for number in range(1, 65):
        total_grains = total_grains + square(number)
    return total_grains


print(square(2))
print(total())