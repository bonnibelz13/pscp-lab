""" test """
import math


def main():
    """ _ """
    work = int(input())
    sumhour = 0
    for _ in range(work):
        hour = float(input())
        sumhour += hour
    pay = (8720 * math.ceil(sumhour))
    print(pay)
main()
