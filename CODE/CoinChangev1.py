''' CoinChangev1 '''
def coinchange():
    ''' จำนวนเหรียน ทอนเงินสับๆจร๊ะ '''
    money = int(input())
    twenty_five, left = divmod(money, 25)
    ten, left = divmod(left, 10)
    five, one = divmod(left, 5)
    print(twenty_five + ten + five + one)
coinchange()
