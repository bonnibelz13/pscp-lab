""" Pringles """
def main():
    """ hiw """
    toppack = input()
    pingle = input()
    bottompack = input()
    finger = int(input())
    eat = pingle.count(')', None, finger)
    leftpingle = ' ' * finger + pingle[finger:]
    left = leftpingle.count(')')
    print(eat)
    if left > 0:
        print('There are still some left.')
    elif left <= 0:
        print('None.')
    print(toppack)
    print(leftpingle)
    print(bottompack)
main()
