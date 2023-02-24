""" Pringles """
def main():
    """ hiw """
    toppack = input()
    pingle = input()
    bottompack = input()
    finger = int(input())
    eat = pingle.count(')', None, finger)
    leftpingle = pingle.count(')') - eat
    print(eat)
    if leftpingle > 0:
        print('There are still some left.')
    elif leftpingle <= 0:
        print('None.')
    print(toppack)
    print(' ' * finger + pingle[finger:])
    print(bottompack)
main()
