""" test """
import math
def main():
    """ cal """
    firstq = float(input())
    secondq = float(input())
    firstp = float(input())
    secondp = float(input())
    euclidean = math.sqrt((firstq - firstp)**2 + (secondq - secondp)**2)
    print(euclidean)
main()
