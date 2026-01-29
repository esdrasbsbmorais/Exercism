def leap_year(year):
    return (year & 3 == 0 and year % 100 != 0) or (year % 400 == 0)
    pass
