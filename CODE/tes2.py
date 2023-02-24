def perfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
    return (True if sum == n and n!=1 else False)
def main():
    ''' '''
    num = int(input())
    i = 2
    total = 0
    for i in range(num):
        if perfect(i):
            total += i
    print(total)
main()