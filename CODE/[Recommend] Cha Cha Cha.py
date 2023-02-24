""" [Recommend] Cha Cha Cha """
import math

def main():
    """ payment """
    work = int(input())
    pay = 0
    for _ in range(work):
        hour = float(input())
        pay += 8720 * (math.ceil(hour))
    print(pay)
main()
