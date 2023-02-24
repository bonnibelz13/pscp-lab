""" This is Stepper II """


def stepperii():
    """ print ori-num"""
    ori = int(input())
    num = int(input())
    if num >= ori:
        for i in range(ori, num + 1):
            print(i)
    elif num <= ori:
        for i in range(ori, num - 1, -1):
            print(i)
stepperii()
