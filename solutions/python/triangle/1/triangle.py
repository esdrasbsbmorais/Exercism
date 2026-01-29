def equilateral(sides):
    a, b, c = sides
    if (a > 0 and b > 0 and c > 0) and (a == b == c):
        return True
    else:
        return False
    pass


def isosceles(sides):
    a, b, c = sides
    if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a) and (a == c or b == c or b == a):
        return True
    else:
        return False
    pass


def scalene(sides):
    a, b, c = sides
    if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a) and (a != b and a != c and b != c):
        return True
    else:
        return False
    pass
