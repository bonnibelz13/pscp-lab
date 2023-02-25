"""code"""


def code():
    """code"""
    num1 = (input())
    change1 = 10 - int(len(num1))
    code1 = (("0" * change1) + num1)

    num2 = (input())
    change2 = 10 - int(len(num2))
    code2 = (("0" * change2) + num2)

    num3 = (input())
    change3 = 10 - int(len(num3))
    code3 = (("0" * change3) + num3)

    num4 = (input())
    change4 = 10 - int(len(num4))
    code4 = (("0" * change4) + num4)

    num5 = (input())
    change5 = 10 - int(len(num5))
    code5 = (("0" * change5) + num5)
    print(code1, end="\n")
    print(code2, end="\n")
    print(code3, end="\n")
    print(code4, end="\n")
    print(code5, end="\n")


code()
