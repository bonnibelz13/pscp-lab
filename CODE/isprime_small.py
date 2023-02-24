''' isprime_small '''
def isprime():
    ''' ตัวเลขที่ใส่เข้าไปเป็น จำนวนเฉพาะ หรือไม่ '''
    num = int(input())
    if num > 1:
        for _ in range(2, num):
            if (num % _) == 0:
                print('NO', num **0.5)
                break
        else:
            print('YES')
    else:
        print('NO')
isprime()
#142412125