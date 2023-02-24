""" Sequence IV """

def main():
    """ ตัวตึงจัดๆ """
    num = int(input())
    start = 1
    for _ in range(num):
        for _ in range(num):
            print(start, end=" ")
            start += 1
        print()
main()
