"""Seven"""


def main():
    """find unit of 7 exponent"""
    exponent = int(input())
    if exponent % 4 == 0:
        print("1")
    elif exponent % 4 == 1:
        print("7")
    elif exponent % 4 == 2:
        print("9")
    elif exponent % 4 == 3:
        print("3")
main()


# or
""" _ """
 
def main():
    """ minimal ECKSDEE """
    print([7, 9, 3, 1][(int(input()) - 1) % 4])
main()