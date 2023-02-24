''' Day2011 '''
def weekDay(year, day, month):
    ''' year = 2011 , find day of week '''
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Friday', 'Saturday']
    afterFeb = 1
    if month > 2:
        afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayofweek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayofweek += (aux + afterFeb) * 365
    # leap year correction
    dayofweek += aux / 4 - aux / 100 + (aux + 100) / 400
    # sum monthly and day offsets
    dayofweek += offset[month - 1] + (day - 1)
    dayofweek %= 7
    return week[int(dayofweek)]
print(weekDay(year=2011, day=int(input()), month=int(input())))
