''' FibonacciRecursionV2 '''
def fibo(num, dictfibo):
    ''' f(n) = f(n-1) + f(n-2) '''
    if num not in dictfibo:
        if num > 500:   #แก้case num 1000+   แต่ num 249757+ ไม่ได้
            fibo(num - 500, dictfibo)
        dictfibo[num] = fibo(num-1, dictfibo) + fibo(num-2, dictfibo)
    return dictfibo[num]
def main():
    ''' input and print '''
    dictfibo = {0:0, 1:1}
    num = int(input())
    total = fibo(num, dictfibo)
    print(total)
main()
