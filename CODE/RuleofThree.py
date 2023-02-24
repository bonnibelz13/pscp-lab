""" RuleofThree """
def snack():
    """ คุ้มคุ้ม """
    num = int(input())
    min_price = 999999999999999999999999999999999999999999999999999
    for _ in range(num):
        price = float(input())
        weight = float(input())
        pay = price / weight
        if pay <= min_price and pay != 0 and pay > 0:
            min_price = pay
            buy = price
            min_weight = weight
    print('%.2f %.2f' %(buy, min_weight))
snack()
