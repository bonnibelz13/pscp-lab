
from operator import concat, floordiv


def myFunction():
    num = int(input())
    bitStr = ""
    while num != 0:
        remain = num % 2
        num = floordiv(num, 2)
        bitStr = concat(str(remain), bitStr)
    return bitStr

myFunction()