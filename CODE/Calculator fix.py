''' Calculator V2 '''
def cal():
    ''' cal plus '''
    num = int(input())
    total = 0
    while num >= 1:
        if num == 1:
            total = 1
            break

        #หา 9 * lenของnum
        num_minus_nine = '9' * (len(str(num)) - 1)
        if num_minus_nine == '':    #กรณีเลข 1 ถึง 9
            num_minus_nine = 0

        #num - 9 * lenของnum
        total += (num - int(num_minus_nine)) * (len(str(num)) + 1)
        num -= (num - int(num_minus_nine))
    print(total)
cal()
