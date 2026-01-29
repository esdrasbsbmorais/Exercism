def equilateral(sides):
    a, b, c = sides
    return is_valid_triangle(a, b, c) and (a == b == c)


def isosceles(sides):
    a, b, c = sides
    return is_valid_triangle(a, b, c) and (a == c or b == c or b == a)


def scalene(sides):
    a, b, c = sides
    return is_valid_triangle(a, b, c) and (a != b and a != c and b != c)

def is_valid_triangle(a, b, c):
    return (a > 0 and b > 0 and c > 0) and (a + b > c and b + c > a and c + a > b)