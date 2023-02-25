"""ฺBinaryปิด/เปิด"""


def binary_function():
    """0 คือ close 1 คือ open input จากเลขฐาน10"""
    num = int(input())
    if num < 51:
        x = bin(num)
        x = (x[2::])
        print(x[0:])

        print(x.count("1"))
        print(x.count("0"))


binary_function()

