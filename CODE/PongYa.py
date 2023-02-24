''' PongYa '''
def pong():
    ''' if txt[-1] == 3 or % 3 == 0 print Pong else print number '''
    txt = int(input())
    #print(str(txt)[-1]) ตัวสุดท้าย เป็น3อะป่าว
    if str(txt)[-1] == '3' or txt % 3 == 0:
        print('PONG')
    else:
        print(txt)
pong()
