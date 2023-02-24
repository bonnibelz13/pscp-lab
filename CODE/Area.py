''' Area '''
def area():
    ''' จงหาพื้นที่แรเงาของรูป '''
    col = int(input())
    pic = [input() for _ in range(col)]
    pic = ''.join(pic)
    countpic = 0
    for i in pic:
        if i != ' ':
            countpic += 1
    #print(pic, sep='\n') ดูlist pic
    print(countpic)
area()
