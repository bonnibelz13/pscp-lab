"""Squareroot"""


def main():
    """is x sqr y if yes = true"""
    num_x = float(input())
    num_y = float(input())
    if num_x**2 == num_y:
        print(True)
    elif num_x**2 != num_y:
        print(False)
main()
