"""This is Donut"""


def howmuch():
    """ how much to pay and how many donut will we get"""
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    i = 1
    donut = b + c
    while a > 0 and b > 0 and c >= 0 and d >= 0:
        if donut < d:
            i += 1
            donut = (b + c) * i
        elif donut >= d:
            paid = (a * b) * i
            print(paid, donut)
            break
howmuch()
