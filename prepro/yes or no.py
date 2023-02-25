"""มีตัวอักษรพิเศษไหมคะ"""


def find_special():
    """ถ้ามีเป็นno ถ้าไม่มีเป็นyes"""

    text = input()
    if text.isalnum():
        print("Yes, it is.")
    else:
        print("No, it's not.")

find_special()
