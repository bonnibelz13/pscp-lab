"""Surprising"""

all = float(input())
mak = float(input())
def som(gang, noi):
    """find min"""
    if mak + gang + noi != all and gang < mak and noi < mak and mak < 11:
        gang += 1
        som(gang, noi)
    elif mak + gang + noi != all and gang == mak and noi < mak and mak < 11:
        noi += 1
        som(gang, noi)
    elif mak + gang + noi == all:
        print(gang, noi)
        minus = mak - noi
        if minus > 2:
            print("Surprising")
        elif minus <= 2:
            print("Not surprising")
def loop():
    """ do loop"""
    som(0, 0)
loop()