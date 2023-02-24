""" LargestNumber """

def main():
    """ เรียงเลขให้มีค่ามากที่สุด"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 >= 0 and num2 >= 0 and num3 >= 0:
        if num1 >= num2 >= num3:
            xxx = print(num1, num2, num3, sep='')
        elif num1 >= num3 >= num2:
            yyy = print(num1, num3, num2, sep='')
        elif num2 >= num1 >= num3:
            zzz = print(num2, num1, num3, sep='')
        elif num2 >= num3 >= num1:
            aaa = print(num2, num3, num1, sep='')
        elif num3 >= num1 >= num2:
            bbb = print(num3, num1, num2, sep='')
        elif num3 >= num2 >= num1:
            ccc = print(num3, num2, num1, sep='')
main()
