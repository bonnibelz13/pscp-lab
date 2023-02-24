''' Coke '''
def coke():
    ''' coke promotion '''
    oldprice = int(input())
    cap = int(input())
    proprice = int(input())
    want = int(input())
    bot = 0
    total = 0
    havecap = 0
    price = oldprice
    while bot != want:
        total += price
        price = oldprice
        havecap += 1
        if cap == 0:
            total = price*want
            break
        if havecap == cap:
            price = proprice
            havecap -= cap
        bot += 1
    print(total)
coke()
