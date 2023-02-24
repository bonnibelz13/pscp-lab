""" Sequence V """

def main():
    """ ตัวตึงเหี้ยๆ """
    num = int(input())
    for _ in range(num):
        if num < 1:
            break
        for _ in range(7):
            if num < 1:
                break
            print(num, end=" ")
            num -= 1
        print()
main()
