"""เค้กช็อกโกแลต"""


def chocolate():
    """coco"""
    money = int(input())
    price = int(input())
    chocolate_cake = money // price
    if chocolate_cake > 0:
        print("Chocolate Cake:", chocolate_cake)
        print("Money left:", money - (chocolate_cake*price))
    elif chocolate_cake <= 0:
        print("Not enough money;(")
        print("Money left:", money)


chocolate()
