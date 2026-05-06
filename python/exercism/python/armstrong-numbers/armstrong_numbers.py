def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    armstrong = [int(digit) ** power for digit in digits]
    total = sum(armstrong)
    return total == number 

print(is_armstrong_number(153))

