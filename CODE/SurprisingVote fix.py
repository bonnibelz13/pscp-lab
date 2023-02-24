""" This is SurprisingVote"""

def main():
    """ find noi"""
    total = float(input())
    mak = float(input())
    noi = total - mak - mak
    if noi < 0:
        noi = 0
    while 0 <= total <= 30 and 0 <= mak <= 10:
        if mak - noi > 2:
            print("Surprising")
            break
        elif mak - noi <= 2:
            print("Not surprising")
            break
main()
