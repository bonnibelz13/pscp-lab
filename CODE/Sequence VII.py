""" Sequence VII """

def main():
    """ pyramid of number"""
    num = int(input())
    i = 1
    for i in range(1, num+1):
        for i in range(1, i+1):
            print(i, end=" ")
        print()
    for i in range(num+1, 1, -1):
        for j in range(1, i-1):
            print(j, end=" ")
        print()
main()
