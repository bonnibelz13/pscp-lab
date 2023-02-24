''' Ink '''
import math
def ink():
    ''' อัตราการขยายพื้นที่ของน้ำหมึก '''
    xxx, yyy = [int(i) for i in input().split()]
    area = []
    for _ in range(yyy):
        posx, posy = [int(k) for k in input().split()]
        circle = (posx**2 + posy**2)**0.5
        circle = 3.1416 * circle**2
        area.append(circle)
    for total in area:
        print(math.ceil(total/xxx))
ink()
