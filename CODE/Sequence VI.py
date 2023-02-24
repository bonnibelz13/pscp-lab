""" Sequence VI """

def main():
    """ pyramid of number"""
    num = int(input())
    i = 1
    for i in range(1, num+1):
        for i in range(1, i+1):
            print(i, end=" ")
        print()
main()
