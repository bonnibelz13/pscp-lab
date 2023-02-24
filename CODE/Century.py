""" Century """
import math

def century(numyear):
    """ ศตวรรษ """
    numyear = math.ceil(numyear * 0.01)
    if numyear > 0:
        return numyear
    else:
        return 'ERROR'
def main():
    """ year to century """
    num = int(input())
    for _ in range(num):
        year = input()
        if year[0:4] == 'B.E.':
            numyear = int(year[5:]) - 543
        elif year[0:4] == 'A.D.':
            numyear = int(year[5:])
        print(century(numyear))
main()
