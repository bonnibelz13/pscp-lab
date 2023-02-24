''' isprime_large '''
def is_prime(num):
    ''' ตัวเลขที่ใส่เข้าไปเป็น จำนวนเฉพาะ หรือไม่ '''
    if num <= 1:
        return 'NO'
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 'NO'
    print('YES')
    quit()
print(is_prime(num=int(input())))
