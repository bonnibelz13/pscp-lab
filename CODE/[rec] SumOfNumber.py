""" test """
def main():
    want = int(input())
    num = int(input())
    sumnum = 0
    while num > -1 and want > -1:
        sumnum += num
        if sumnum == want:
            break
        num = int(input())
    print(sumnum)
main()
