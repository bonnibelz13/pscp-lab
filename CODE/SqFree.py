''' SqFree '''
def sqfree(i):
    ''' if i is sqfreenum return True else False '''
    if i % 2 == 0:
        i = i / 2
    if i % 2 == 0:
        return False

    for k in range(3, int(i**0.5 + 1)):
        if i % k == 0:
            i = i / k
        if i % k == 0:
            return False
    return True

def main():
    ''' input and print '''
    num = int(input())
    sqnum = 0
    for i in range(num+1):
        if sqfree(i) == True:
            sqnum += 1
    print(sqnum)
main()
