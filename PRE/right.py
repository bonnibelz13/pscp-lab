"""This is RightArrow"""


def arrow_function():
    """print right arrow"""
    wide = int(input())  # wide of *
    height = int(input())  # only odd number
    if height % 2 == 0:
        return 0
    for i in range(height):
        if i > height // 2:
            for _ in range(height-(i+1)):
                print(" ", end="")
            for _ in range(wide):
                print("*", end="")
            print()
        else:
            for _ in range(i):
                print(" ", end="")
            for _ in range(wide):
                print("*", end="")
            print()


arrow_function()
