def dow(year, day, month):
    """ day of week, Sunday = 0, Saturday = 6 """
    week   = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Friday', 'Saturday']
    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1
    K = year % 100
    J = year // 100
    f = (day + int(13*(month + 1)/5.0) + K + int(K/4.0))
    fg = f + int(J/4.0) - 2 * J
    fj = f + 5 - J
    if year > 1582:
        h = fg % 7
    else:
        h = fj % 7
    if h == 0:
        h = 7
    return week[h-1]
print(dow(year=2011, day=int(input()), month=int(input())))