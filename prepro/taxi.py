""" Taxi Rate """
def rate():
    """ input kilo & time """
    kilo = int(input())
    sec = int(input())
    minute = 0
    price = 0
    if kilo > 0:
        price = price + 50
    if kilo > 1:
        price = price + 5*min(kilo-1, 9)
    if kilo > 10:
        price = price + 7.5*min(kilo-10, 10)
    if kilo > 20:
        price = price + 10*min(kilo-20, 20)
    if kilo > 40:
        price = price + 12.5*min(kilo-40, 25)
    if kilo > 65:
        price = price + 15*(kilo-65)
    if sec%60 != 0:
        minute = minute +1
    minute = minute + sec//60
    price = price + minute * 1.5
    if price % 1 != 0:
        price = int(price) +1
        print(price)
    else:
        print(round(price))
rate()