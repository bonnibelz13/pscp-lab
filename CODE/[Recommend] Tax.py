''' [Recommend] Tax '''
def tax():
    ''' ภาษีรถยนต์ '''
    year = int(input())
    car_cc = int(input())
    dis = 0
    pay = 0
    if year >= 6:
        disyear = year - 5
        dis = 10 * disyear
    if year >= 10:
        dis = 50
    if car_cc <= 600:
        pay += car_cc * 0.5
    elif car_cc <= 1800:
        pay += ((car_cc - 600) * 1.5) + 300
    elif car_cc > 1800:
        pay += ((car_cc - 1800) * 4) + 2100
    if dis != 0:
        print('%.2f'%(pay - (pay * (dis/100))))
    else:
        print('%.2f'%pay)
tax()
