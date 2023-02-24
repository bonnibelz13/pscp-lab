''' Difference '''
def diff():
    ''' สมาชิกทั้งหมดของเซต A-B '''
    line_a = int(input())
    line_b = int(input())
    set_a = {int(input()) for _ in range(line_a)}
    set_b = {int(input()) for _ in range(line_b)}
    set_c = set_a - set_b
    print(*sorted(set_c))
diff()
