''' temperature '''
def tem():
    ''' 0 '''
    num = float(input())
    txt_1 = input()
    txt_2 = input()

    if txt_1 == 'F':
        num = (num - 32) * 5/9
    elif txt_1 == 'K':
        num -= 273.15
    elif txt_1 == 'R':
        num = (num - 491.67) * 5/9

    if txt_2 == 'F':
        num = (num * 9/5) + 32
    elif txt_2 == 'K':
        num += 273.15
    elif txt_2 == 'R':
        num = (num * 9/5) + 491.67
    print('%.2f' %num)
tem()
