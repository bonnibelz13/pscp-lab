""" Sequence III """


def main():
    num = int(input())
    n = 0
    for i in range(2, num+2):
        if n != num:
            print(i, sep=" ")
            i += 1
        elif n == num:
            break
main()






