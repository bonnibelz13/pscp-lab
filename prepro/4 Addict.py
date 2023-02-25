"""This is 4 Addict"""


def print_4addict():
    """are you crazy"""
    var_x = float(input())
    y = 44
    var = var_x >= y
    text = str(input())
    cal = ((((var_x + 4) ** 0.25) + (var_x / 4)) / (4 * var_x - 4)) * 44
    count = int(var_x // 44)

    print(text * count)
    print('%0.4f' % cal)


print_4addict()
