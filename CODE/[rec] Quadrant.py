""" test """
def quadrant(xxx, yyy):
    """ check xxx and yyy quadrant """
    if xxx == 0 and yyy == 0:
        return 'O'
    elif xxx == 0 and yyy > 0:
        return 'X'
    elif xxx > 0 and yyy == 0:
        return 'Y'
    elif xxx > 0 and yyy > 0:
        return 'Q1'
    elif xxx > 0 and yyy < 0:
        return 'Q2'
    elif xxx < 0 and yyy < 0:
        return 'Q3'
    elif xxx < 0 and yyy > 0:
        return 'Q4'
def main():
    """ intput xxx and yyy to print quadrant """
    xxx = int(input())
    yyy = int(input())
    print(quadrant(xxx, yyy))
main()
