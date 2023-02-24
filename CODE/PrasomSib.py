''' PrasomSib '''
def prasomsib():
    ''' จำนวนวิธีที่จะหาผลรวมให้ได้สิบ ของตัวเลขโดดที่อยู่ติดกัน '''
    num = input()
    numlong = len(num)
    total = 0
    for i in range(numlong - 1):
        count = 0
        for j in num[int(i):]:
            count += int(j)
            if count == 10:
                total += 1
                break
    print(total)
prasomsib()
