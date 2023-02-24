""" Ball """


def main():
    """ Ball"""
    num = float(input())
    total = -1
    while num >= 0.01:
        num = num * 3/5
        total += 1
    print(total)


main()
