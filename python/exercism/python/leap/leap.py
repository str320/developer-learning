def leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(leap_year(1997))
print(leap_year(1900))
print(leap_year(2000))
