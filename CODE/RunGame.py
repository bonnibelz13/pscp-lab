''' RunGame '''
def rungame():
    ''' เป็นระยะทางรวมที่ต้องวิ่ง '''
    run = input().split()
    distance = 0
    already_run = 0
    for i in run:
        distance = abs(int(i) - distance)
        already_run += distance
        distance = int(i)
    print(already_run)
rungame()
