"""TheFunctionWithin"""


def find_function():
    """หาฟังก์ชั่นที่กำหนด"""
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
    var_a = 2 * var_a
    var_b = 2 * var_b
    var_c = 2 * var_c
    var_d = 2 * (var_d)**2
    print(2 * var_a)
    print(3 * (var_a - var_b)**4 - (var_a - var_b)**3 + 2 * (var_a - var_b)**2 + 10)
    gd_two = (3 * (var_d)**4) - ((var_d)**3) + (2 * (var_d)**2) + 10
    print((gd_two + (var_a + var_b))**2 - ((var_a + var_b)*(var_a + var_c)) + ((var_a + var_c))**2)
    var_z = 3 * (var_d)**4 - (var_d)**3 + 2 * (var_d)**2 + 10
    h_xyz = (var_z + (var_a + var_b))**2 - ((var_a + var_b) * (var_a - var_c)) + (var_a - var_c)**2
    func_gx = 3 * (var_a - var_b)**4 - (var_a - var_b)**3 + 2 * (var_a - var_b)**2 + 10
    func_fc = (((var_c*2)*2)*2)*2
    var_d = ((var_d / 2)**0.5)**8
    print(((h_xyz)**2 + (func_gx)**2 - func_fc**2) / ((var_d)**2 - 2 * (h_xyz * var_d) + 2 * h_xyz))

find_function()
