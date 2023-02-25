""""Restaurant"""


def hiwkaw():
    """หนูอยากกลับบ้าน"""
    age = int(input())
    dish = int(input())

    if age >= 60 and dish == 1:
        print("Free")
    elif age >= 60 and dish > 1:
        price = int((dish * 100) / 2)
        print("Pay", price, "baht")
    else:
        price = int(dish * 100)
        print("Pay", price, "baht")

hiwkaw()
