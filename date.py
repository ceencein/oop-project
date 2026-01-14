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

def date_diff(date_input):

    date1, date2 = date_input.split(',')
    first_date = date1.split('-')
    sec_date = date2.split('-')

    day_input1 = int(first_date[0])
    month_input1 = int(first_date[1])
    year_input1 = int(first_date[2])

    day_input2 = int(sec_date[0])
    month_input2 = int(sec_date[1])
    year_input2 = int(sec_date[2])

    if (day_of_year(day_input1, month_input1, year_input1) == False or 
       day_of_year(day_input2,month_input2,year_input2) == False ):
        print("Invalid")
    
    elif (day_input1 == day_input2 and month_input1 == month_input2 and year_input1 == year_input2):
        print("1")
    
    elif (year_input1 == year_input2):
        totaldiff = day_of_year(day_input2, month_input2, year_input2) - \
                day_of_year(day_input1, month_input1, year_input1) + 1
        
        print(totaldiff)

    else:
        first_distance = (day_in_year(year_input1) - day_of_year(day_input1, month_input1, year_input1)) + 1
        #print(f"{first_distance} = {day_in_year(year_input1)} - {day_of_year(day_input1,month_input1,year_input1)}")

        sec_distance = day_of_year(day_input2, month_input2, year_input2)
        #print(f"{sec_distance}")

        middle_days = 0
        if (year_input2 - year_input1) > 1:
            for y in range(year_input1 + 1, year_input2):
                middle_days += day_in_year(y)

        totaldiff = first_distance + sec_distance + middle_days

        print(f"{totaldiff}")

def day_in_year(year):

    if is_leap(year):
        return 366
    else :
        return 365