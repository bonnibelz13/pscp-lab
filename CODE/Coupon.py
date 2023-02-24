''' Coupon '''
def coupon():
    ''' หา coupon ที่ใช้แล้วลดเยอะสุดจร้ '''
    price = float(input())
    cou1 = input()
    cou2 = input()

    disprice1, minprice1 = [float(_) for _ in cou1.split()]
    disprice2, minprice2 = [float(_) for _ in cou2.split()]
    pay1 = price
    pay2 = price

    if price >= minprice1:
        pay1 = max(0, price - disprice1)

    if price >= minprice2:
        pay2 = max(0, price - (price * (disprice2/100)))

    if price < minprice1 and price < minprice2:
        print('Nope')
    elif pay1 == pay2:
        if minprice1 < minprice2:
            print(1, '%.1f'%pay1)
        elif minprice2 < minprice1:
            print(2, '%.1f'%pay2)
        elif minprice1 == minprice2:
            print(1, '%.1f'%pay1)
    elif pay1 < pay2 and pay1 < price:
        print(1, '%.1f'%pay1)
    elif pay2 < pay1 and pay2 < price:
        print(2, '%.1f'%pay2)
coupon()
