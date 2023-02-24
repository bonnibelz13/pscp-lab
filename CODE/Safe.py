''' Safe '''
def safe():
    ''' จำนวนครั้งที่หมุนช่องตัวอักษรที่น้อยที่สุด '''
    pw_1 = input()
    pw_2 = input()
    num_turning = 0
    for i in range(len(pw_1)):
        front = abs(ord(pw_1[i]) - ord(pw_2[i]))
        back = 26 - front
        if front < back:
            num_turning += front
        else:
            num_turning += back
    print(num_turning)
safe()
