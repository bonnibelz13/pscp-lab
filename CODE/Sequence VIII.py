""" Sequence VIII """

def main():
    """ pyramid of number """
    rows = int(input())
    if 0 < rows < 100:
        for i in range(1, rows+1):
            num = 1
            for j in range(rows, 0, -1):
                if j > i:
                    print(" ", end='  ')
                else:
                    print('%02d' % num, end=' ')
                    num += 1
            print()
main()
