cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = "audi"

if car == "bmw":
    print(car.title())
else:
    print(f"\nThis is an {car} car!")

if car != "bmw":
    print(f"\nThis is an {car} car!")

# Checking Multiple Conditions

age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 >= 21:
    print("\nTrue")
else:
    print("\nFalse")

age_1 = 22

if age_0 >= 21 and age_1 >= 21:
    print(f"\nage: {age_1}, True")
else:
    print("False")

age_0 = 18

if age_0 >= 21 or age_1 >= 21:
    print(f"\nage: {age_0}, True")



