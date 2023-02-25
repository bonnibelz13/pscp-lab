


width = 4
length = 4
height = 2

box_area = width * length * height
print(box_area)

'''
สร้าง function ขึ้นมาเอง
วิธีทำ
def ชื่อฟังก์ชั่น():
    คำสั่งข้างใน
'''

def function_box_area():                            #def เป็นการกำหนดฟังก์ชั่นขึ้นมาเอง function_box_area(): คือชื่อฟังก์ชั่นที่เราตั้งเอง
    width = 4
    length = 4
    height = 2
    box_area = width * length * height
    print(box_area)

function_box_area()                                 ##อย่าลืมพิมพ์อันนี้ คือการเรียกใช้ฟังก์ชั่นที่เราทำขึ้นมาเอง ***


'''
ใช้ พารามิเตอร์ มาช่วย พารามิเตอร์จะนำค่าจากข้างนอกมาใช้ในฟังก์ชั่น จะมีกี่ตัวก็ได้ หรือจะไม่มีก็ได้
วิธีทำ
def ชื่อฟังก์ชั่น(พารา1, พารา2, พารา3):
    คำสั่งข้างใน
'''

def function_box_area(width, length, height):       #def เป็นการกำหนดฟังก์ชั่นขึ้นมาเอง function_box_area(): คือชื่อฟังก์ชั่นที่เราตั้งเอง
    box_area = width * length * height
    print(box_area)

function_box_area(4, 4, 2)                          #เวลาเรียกใช้ฟังก์ชั่น ต้องใส่ค่าตัวเลข ให้ตรงตามตัวแปรพารามิเตอร์ในคำสั่งฟังก์ชั่น run จะได้ 32
function_box_area(3, 5, 10)                         #สามารถกำหนดได้หลายตัวเลข run จะได้ 150
function_box_area(width=3, length=5, height=10)     #ถ้ากลัวลืมตัวแปรพารามิเตอร์ ก็เขียนกำหนดได้ ตัวแปร=ค่าที่ต้องการ run จะได้ 150


'''
ใช้คำสั่ง return
จะคืนค่าคำสั่งกลับไป
วิธีทำ
def ชื่อฟังก์ชั่น(พารา1, พารา2, พารา3):
    คำสั่งข้างใน
    return กำหนดคำสั่งที่เราต้องการให้เราคืนค่าไป หรือ กำหนดสิ่งที่เราต้องการให้แสดงผลออกมา
กำหนดตัวแปร = ชื่อฟังก์ชั่น(พารา1, พารา2, พารา3):
print(ตัวแปร)
'''

def function_box_area(width, length, height):                   #def เป็นการกำหนดฟังก์ชั่นขึ้นมาเอง function_box_area(): คือชื่อฟังก์ชั่นที่เราตั้งเอง
    box_area = width * length * height
    return box_area                                             #return เป็นการคืนค่าคำสั่งที่เรากำหนดฟังก์ชั่นไว้กลับไปทำให้เมื่อ print() จะสามารถกำหนดตัวแปรและนำมาคำนวณได้

box1 = function_box_area(4, 4, 2)                               #กำหนดตัวแปร boxแต่ละอัน คือ ค่าพื้นที่ที่นำมาคำนวณ ได้จาก ฟังก์ชั่นที่เรากำหนดและใส่ค่าตัวเลขที่ต้องการลงพารามิเตอร์
box2 = function_box_area(3, 5, 10)
box3 = function_box_area(width=3, length=5, height=10)

print(box1, box2, box3)                                         #run จะได้ 32 150 150


'''
ใช้คำสั่ง return และ มีเงื่อนไข if
จะคืนค่าคำสั่งกลับไป
วิธีทำ
def ชื่อฟังก์ชั่น(พารา1, พารา2, พารา3):
    if เงื่อนไขที่ต้องการกำหนด:
    คำสั่งข้างใน
    return กำหนดคำสั่งที่เราต้องการให้เราคืนค่าไป หรือ กำหนดสิ่งที่เราต้องการให้แสดงผลออกมา
กำหนดตัวแปร = ชื่อฟังก์ชั่น(พารา1, พารา2, พารา3):
print(ตัวแปร)
'''

def function_box_area(width, length, height):                   #def เป็นการกำหนดฟังก์ชั่นขึ้นมาเอง function_box_area(): คือชื่อฟังก์ชั่นที่เราตั้งเอง
    if width < 0 or length < 0 or height <0:
        return 0
    box_area = width * length * height
    return box_area                                             #return เป็นการคืนค่าคำสั่งที่เรากำหนดฟังก์ชั่นไว้กลับไปทำให้เมื่อ print() จะสามารถกำหนดตัวแปรและนำมาคำนวณได้

box1 = function_box_area(4, 4, 2)                               #กำหนดตัวแปร boxแต่ละอัน คือ ค่าพื้นที่ที่นำมาคำนวณ ได้จาก ฟังก์ชั่นที่เรากำหนดและใส่ค่าตัวเลขที่ต้องการลงพารามิเตอร์
box2 = function_box_area(3, 5, 10)
box3 = function_box_area(width=3, length=5, height=10)

print(box1, box2, box3)                                         #run จะได้ 32 150 150
