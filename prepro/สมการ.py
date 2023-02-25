"""this is equation"""


def print_equation():
    """equation"""
    var_a = int(input())
    var_b = int(input())
    var_c = int(input())
    var_d = int(input())
    var_x = int(input())
    var_y = int(input())
    var_z = (((var_b/(var_a**2/var_d))+(var_x*(var_b/var_a)))*var_y)/(var_y*var_c)
    print('%.2f' % var_z)


print_equation()
