''' ClockHands '''
def clock():
    ''' คำนวณว่าเข็มทั้งสองกำลังจะทับกัน \
        เข็มชั่วโมงอยู่ข้างหน้า (นับจากตำแหน่ง 12 นาฬิกา ไปทางตามเข็มนาฬิกา)\
        หรืออยู่ที่ตำแหน่งเดียวกับเข็มนาทีมุมระหว่างเข็มชั่วโมงกับเข็มนาที\
        มีขนาดน้อยกว่ามุมระหว่างรอยขีดนาทีไปจนถึงขีดนาทีถัดไป '''
    hour = int(input())
    second = int(input())
    hour = ((hour * 5) + (second / 12)) % 60
    if hour >= second and hour < second + 1:
        print(True)
    else:
        print(False)
clock()
