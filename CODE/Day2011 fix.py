''' Day2011 '''
def day_of_week(year, day, month):
    ''' print day of week '''
    numday = 0
    if month < 3:
        month += 12
        year -= 1
    if month == 12:
        numday -= 1
    numday += (day + (int((13 * (month - 2))/5)) + year \
        + (int(year/4)) - (int(year/100))-(int(year/400))) % 7
    return int(numday)
def main():
    ''' day and month input '''
    days = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
    numday = day_of_week(2011, day=int(input()), month=int(input()))
    print(days[numday])
main()
