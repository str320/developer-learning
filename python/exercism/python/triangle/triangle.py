def is_triangle(sides):
    a, b, c = sides
    is_sides_positive = a > 0 and b > 0 and c > 0
    follows_triangle_rule = a + b >= c and b + c >= a and c + a >= b
    return follows_triangle_rule and is_sides_positive


def equilateral(sides):
    a, b, c = sides
    is_equilateral = a == b and b == c
    return is_equilateral and is_triangle(sides)

def isosceles(sides):
    a, b, c = sides
    is_isosceles = a == b or b == c or c == a
    return is_isosceles and is_triangle(sides)


def scalene(sides):
    a, b, c = sides 
    is_scalene = a != b and b != c and c != a
    return is_scalene and is_triangle(sides)


