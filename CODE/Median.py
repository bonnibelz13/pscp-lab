''' Median '''
def mymedian(numlist):
    ''' median '''
    numlist.sort()
    mid = len(numlist) // 2
    return (numlist[mid] + numlist[~mid]) / 2
def main():
    ''' list input '''
    line = int(input())
    numlist = [int(input()) for _ in range(line)]
    med = mymedian(numlist)
    print('%.1f' %med)
main()
