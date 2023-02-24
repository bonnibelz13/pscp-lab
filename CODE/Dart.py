''' Dart '''
def dart():
    ''' เป้ารัศมี 10น. '''
    num = int(input())
    score = 0
    for _ in range(1, num+1):
        pos = input().split(' ')
        posx = pos[0]
        posy = pos[1]
        rad = (int(posx)**2 + int(posy)**2)**0.5  #r^2 = x^2 + y^2
        if rad <= 2:    #r >= 2หน่วย ได้ 5แต้ม
            score += 5
        elif rad > 2 and rad <= 4:
            score += 4
        elif rad > 4 and rad <= 6:
            score += 3
        elif rad > 6 and rad <= 8:
            score += 2
        elif rad > 8 and rad <= 10:
            score += 1
    print(score)
dart()
