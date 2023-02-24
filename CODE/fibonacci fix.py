
''' Fibonacci fix '''
def fibo(num):
    ''' f(n) = f(n-1) + f(n-2) '''
    known = {0:0, 1:1} #เก็บค่าที่รู้แล้ว
    if num in known:
        return known[num]
    res = fibo(num-1) + fibo(num-2)
    known[num] = res
    print(known)
    return res
print(fibo(num=int(input())))


''' Fibo fix shorter by list '''
def fibo2(num):
    ''' '''
    fib = [0, 1]
    for i in range(2,num + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[num]
print(fibo2(num=int(input())))


''' Fibo fix shorter by three numbers '''
def fibo3(num):
    if num in [0, 1]:
        return num
    a, b = 0, 1
    for _ in range(2, num+1):
        c = a + b
        a, b = b, c
    return c
print(fibo3(num=int(input())))