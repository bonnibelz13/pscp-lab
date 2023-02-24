''' isprime_larger '''
def is_prime(num):
    ''' ตัวเลขที่ใส่เข้าไปเป็น จำนวนเฉพาะ หรือไม่ '''
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1, 3):
        if num % i == 0:
            return False
    print(True)
    quit()
print(is_prime(num=int(input())))
