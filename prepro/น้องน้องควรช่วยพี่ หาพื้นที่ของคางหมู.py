"""This is หาพื้นที่คางหมู"""


def print_trapezoidal_area():
    """Function หาพื้นที่คางหมู"""
    height = float(input())
    base_1 = float(input())
    base_2 = float(input())
    ans = (base_1 + base_2)/2 * height
    print("Trapezoidal area = %.2f" %ans)


print_trapezoidal_area()
