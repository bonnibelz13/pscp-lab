""""distance"""


def get_speed(distance, time):
    return distance / time

speed = get_speed(float(input()), int(input()))
print("อัตราเร็วเท่ากับ : %0.3f" % speed)



""" This is สูตรความเร็ว พี่ปวดเอวเจ็บหัวใจ"""


def print_speed():
    """ calculate speed """
    distance = float(input())
    # หน่วยไมล์ทะเล 1 ไมล์ทะเล = 1852 เมตร
    distance_meter = distance * 1852
    print(distance_meter)
    time = int(input())
    time_second = time / 1000
    # หน่วย มิลลิวินาที (1/1000) 1 วิ = 0.001
    # โดยที่เวลาไม่เกิน 10**10 มิลลิวินาที
    print(time_second)
    speed = distance_meter / time_second
    print("อัตราเร็วเท่ากับ : %.3f" % speed, "เมตรต่อวินาที")

print_speed()



x >= 100

print(x)
