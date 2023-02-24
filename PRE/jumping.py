"""This is Jumping"""


def print_output():
    """print Output"""
    return "Output"


def jumping():
    """output and 4 times"""
    for num in range(1, 5):
        print(print_output(), num, sep="")
        print(print_output(), num, sep="")
        print(print_output(), num, sep="")


jumping()
