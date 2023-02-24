""" Hamburger """


def main(left, right):
    """Main Function"""
    meat = (left+right)*2
    print("|"*left + "*"*meat + "|"*right)


main(int(input()), int(input()))
