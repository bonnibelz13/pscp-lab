""" Sequence III """

def main():
    """ ตัวตึง """
    num = int(input())
    start = 2
    for _ in range(num):
        for i in range(start, num + start):
            print(i, end=" ")
        start += 1
        print()
main()
