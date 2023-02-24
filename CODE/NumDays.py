''' NumDays '''
from datetime import date

def numdays():
    ''' จงหาว่า วัน 2 วันในปี 2560 เดียวกัน นั้นแตกต่างกันกี่วัน '''
    dayone = int(input())
    monthone = int(input())
    daytwo = int(input())
    monthtwo = int(input())

    try:
        day1 = date(2017, monthone, dayone)
        day2 = date(2017, monthtwo, daytwo)
    except ValueError:
        print('Impossible')
        quit()
    howlong = abs(day2 - day1)
    print(howlong.days)

numdays()
