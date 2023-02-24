""" Table I """


def main(num):
    """"Main Function"""
    for _ in range(1, num+1):
        print("15 x %d = %d" % (_, 15*_))


main(int(input()))
