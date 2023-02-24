""" LargestNumber fix """


def main():
    """ find the greatest value """
    num1 = input()
    num2 = input()
    num3 = input()
    xxx = num1+num2+num3
    yyy = num1+num3+num2
    zzz = num2+num1+num3
    aaa = num2+num3+num1
    bbb = num3+num1+num2
    ccc = num3+num2+num1
    if int(xxx) < 1 and int(yyy) < 1 and int(zzz) < 1 \
        and int(aaa) < 1 and int(bbb) < 1 and int(ccc) < 1:
        print(0)
    elif int(xxx) >= int(yyy) and int(xxx) >= int(zzz) \
        and int(xxx) >= int(aaa) and int(xxx) >= int(bbb) and int(xxx) >= int(ccc):
        print(xxx)
    elif int(yyy) >= int(xxx) and int(yyy) >= int(zzz) \
        and int(yyy) >= int(aaa) and int(yyy) >= int(bbb) and int(yyy) >= int(ccc):
        print(yyy)
    elif int(zzz) >= int(xxx) and int(zzz) >= int(yyy) \
        and int(zzz) >= int(aaa) and int(zzz) >= int(bbb) and int(zzz) >= int(ccc):
        print(zzz)
    elif int(aaa) >= int(yyy) and int(aaa) >= int(zzz) \
        and int(aaa) >= int(xxx) and int(aaa) >= int(bbb) and int(aaa) >= int(ccc):
        print(aaa)
    elif int(bbb) >= int(yyy) and int(bbb) >= int(zzz) \
        and int(bbb) >= int(aaa) and int(bbb) >= int(xxx) and int(bbb) >= int(ccc):
        print(bbb)
    elif int(ccc) >= int(yyy) and int(ccc) >= int(zzz) \
        and int(ccc) >= int(aaa) and int(ccc) >= int(bbb) and int(ccc) >= int(xxx):
        print(ccc)
main()
