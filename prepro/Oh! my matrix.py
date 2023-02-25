"""this is Oh! my matrix"""


def print_my_matrix():
    """matrix"""
    var_a1 = int(input())
    var_a2 = int(input())
    var_a3 = int(input())
    var_a4 = int(input())

    var_c1 = int(input())
    var_c2 = int(input())
    var_c3 = int(input())
    var_c4 = int(input())
    detA = ((var_a1 * var_a4) - (var_a2 * var_a3))

    detC = ((var_c1 * var_c4) - (var_c2 * var_c3))

    var_b1 = var_c1 - var_a1
    var_b2 = var_c2 - var_a2
    var_b3 = var_c3 - var_a3
    var_b4 = var_c4 - var_a4
    detB = ((var_b1 * var_b4) - (var_b2 * var_b3))
    print('b1:', var_b1)
    print('b2:', var_b2)
    print('b3:', var_b3)
    print('b4:', var_b4)

    D = detA + detB + detC
    print('D: %.2f' % D)


print_my_matrix()
