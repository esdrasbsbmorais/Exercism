def leap_year(year):
    if (year & 3 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    pass
