""" test """
def main():
    """ """
    num = input()
    sumnum = 0
    for i in num:
        sumnum += int(i)
    last = int(num[-3:]) * 10
    key = sumnum + last
    if key > 9999:
        print(str(key)[-4:])
    elif key < 1000:
        print(key + 1000)
    else:
        print(key)
main()
