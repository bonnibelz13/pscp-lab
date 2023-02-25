"""Server"""


def compare():
    """ไม่รูัๆๆๆ"""
    speed_a = int(input())
    time_a = str(input())
    speed_b = int(input())
    time_b = str(input())
    if time_a == "Millisecond":
        var_a = speed_a * 0.001
    elif time_a == "Microsecond":
        var_a = speed_a * 1e-6
    elif time_a == "Nanosecond" and speed_a >= 1000:
        var_a = speed_a * 1e-9
    elif time_a == "Picosecond" and speed_a >= 1000000:
        var_a = speed_a * 1e-12
    if time_b == "Millisecond":
        var_b = speed_b * 0.001
    elif time_b == "Microsecond":
        var_b = speed_b * 1e-6
    elif time_b == "Nanosecond" and speed_b >= 1000:
        var_b = speed_b * 1e-9
    elif time_b == "Picosecond" and speed_b >= 1000000:
        var_b = speed_b * 1e-12
    if var_a < var_b:
        print('Server A, %.6f second' % var_a)
        print('Faster than server B , %d times' % (var_b // var_a))
    elif var_a > var_b:
        print('Server B, %.6f second' % var_b)
        print('Faster than server A , %d times' % (var_a // var_b))
    elif var_a == var_b:
        print("equal")


compare()
