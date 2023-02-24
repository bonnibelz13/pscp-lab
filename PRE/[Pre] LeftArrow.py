"""This is LeftArrow"""


def arrow_function():
    """print left arrow"""
    wide = int(input())  # wide of *
    height = int(input())  # only odd number
    if height % 2 == 0:
        return 0
    for i in range(height):
        if i > height // 2:
            for _ in range(i - (height // 2)):
                print(" ", end="")
            for _ in range(wide):
                print("*", end="")
            print()
        else:
            for _ in range((height // 2) - i):
                print(" ", end="")
            for _ in range(wide):
                print("*", end="")
            print()


arrow_function()
