"""ODD_EVEN"""


def is_odd():
    """odd = true even = false"""
    num = int(input())
    if num % 2 == 0:
        print(False)
    else:
        print(True)
is_odd()
