""" Inflation """
def money():
    """ เงินเฟ้ออออ """
    num = float(input())
    year = int(input())
    future_value = num * (1 + (3.81/100))**year
    three = ('%.3f'%future_value)
    print(three[0:-1])
money()
