"""ตัวอักษรพิเศษ"""


def find_special():
    """มี=no ไม่มี=yes"""
    text = str(input())

    from string import ascii_letters, digits

    if set(text).difference(ascii_letters + digits):
        print("No, it's not.")
    else:
        print("Yes, it is.")


find_special()
