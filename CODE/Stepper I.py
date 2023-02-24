""" This is Stepper I """


def stepper():
    """ print 1-num"""
    num = int(input())
    if num >= 1:
        for i in range(1, num + 1):
            print(i)
stepper()
