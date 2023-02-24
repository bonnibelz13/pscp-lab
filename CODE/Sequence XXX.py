""" Sequence XXX """
def main():
    ''' xxx '''
    num = int(input())
    xnum = int(input())
    for i in range(num):
        if i == 0 or i == num-1:
            for i in range(xnum):
                print('*' * num, end=' ')
            print()
        elif i != 0 or i != num-1:
            for _ in range(xnum):
                for j in range(num):
                    if j == 0 or j == i or j == num - 1 or j == num - 1 - i:
                        print('*', end='')
                    else:
                        print(' ', end='')
                print('', end=' ')
            print()
main()
