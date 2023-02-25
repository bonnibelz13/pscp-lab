"""secret"""


def secret_code():
    """ coding """
    code = int(input())
    num1 = (code // 100000000)
    num2 = (code // 1000000)
    num3 = (code // 10000)
    num4 = (code // 100)
    num5 = code
    print(str(num1 % 10) + str(num2 % 10) + str(num3 % 10) + str(num4 % 10) + str(num5 % 10))


secret_code()
