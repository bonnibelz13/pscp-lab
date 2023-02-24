""" GraderMachine """

def main():
    """ แยกน้ำหนักที่%2ได้"""
    first = int(input())
    last = int(input())
    k = 0
    print('pass : ', end="")
    if first <= last:
        for i in range(first, last+1):
            if i%2 == 0 and i > 0:
                print(i, end=" ")
                k += i
            i += 1
    elif first >= last:
        for i in range(first, last-1, -1):
            if i%2 == 0 and i > 0:
                print(i, end=" ")
                k += i
    print()
    print('Sum : %d' %k, end=" ")
main()


