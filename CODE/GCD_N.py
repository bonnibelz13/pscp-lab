''' GCD_N '''

def gcd_n(numlist):
    ''' greatest commmon factor of n numbers '''
    if len(numlist) <= 1:
        print(*numlist)
        quit()
    else:
        for i in range(len(numlist)-1):
            first_num = numlist[i]
            second_num = numlist[i+1]
            while second_num:
                first_num, second_num = second_num, first_num%second_num
            numlist[i+1] = first_num
        return first_num

def main():
    ''' input and print '''
    num = int(input())
    numlist = [int(input()) for _ in range(num)]
    print(gcd_n(numlist))
main()
