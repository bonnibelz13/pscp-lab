"""Surprising"""
 
all = float(input())
max = float(input())
def som(mid, min):
    """find min"""
    if max + mid + min != all and mid < max and min < max and max < 11:
        mid += 1
        som(mid, min)
    elif max + mid + min != all and mid == max and min < max and max < 11:
        min += 1
        som(mid, min)
    elif max + mid + min == all:
        minus = max - min
        if minus > 2:
            print("Surprising")
        elif minus <= 2:
            print("Not surprising")
def loop():
    """ do loop"""
    som(0, 0)
loop()