"""FoodGrade I"""


def do_loop(i, twen, num):
    """find chick wings"""
    if i < twen:
        chick = int(input())
        if 70 >= chick >= 50:
            num = num + 1
        i = i + 1
        do_loop(i, twen, num)
    elif i == twen:
        print(num)

def main():
    """loop func"""
    do_loop(0, 24, 0)
main()
