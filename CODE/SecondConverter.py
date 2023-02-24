""" SecondConverter """
#
def main():
    """ convert time """
    ksec = int(input())
    second = int(input())
    minute = int(input())
    hour = int(input())
    if ksec >= 0 and second > 0 and minute > 0 and hour > 0:
        _ = ksec // (hour * (minute * second))
        ksec = ksec % (hour * (minute * second))
        hour = ksec // (minute * second)
        ksec %= (minute * second)
        minute = ksec // second
        ksec %= second
        second = ksec
        print("%d:%d:%d" % (hour, minute, second))
    else:
        return 0
main()
