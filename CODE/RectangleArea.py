''' RectangleArea '''
def rec():
    ''' พื้นที่ทับซ้อน '''
    xxx_a, yyy_a = [int(i) for i in input().split()]
    wei_a, hei_a = [int(i) for i in input().split()]
    xxx_b, yyy_b = [int(i) for i in input().split()]
    wei_b, hei_b = [int(i) for i in input().split()]
    recx_a = xxx_a + wei_a
    recy_a = xxx