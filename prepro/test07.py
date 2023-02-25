

'''
คำนวณพื้นที่ของรูปเลขาคณิตฯ
'''


def get_circle_area(radius):
    return 22/7 * (radius ** 2)

def get_triangle_area(width, height):
    return 1/2 * width * height

def get_rectangle_area(width, height):
    return width * height


circle = get_circle_area(10)
print(circle)

triangle = get_triangle_area(5, 6)
print(triangle)

rectangle = get_rectangle_area(2, 2)
print(rectangle)

'''
อยากเก็บไฟล์ทั้งหมดที่ใช้คำนวณพื้นที่ของรูปเลขาคณิตฯ
'''

