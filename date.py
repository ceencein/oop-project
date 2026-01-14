def is_leap(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)

def day_of_year(day, month, year):

    dim = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    if is_leap(year):
        dim[2] = 29

    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= dim[month]):
        return False

    total = sum(dim[1:month]) + day
    return total