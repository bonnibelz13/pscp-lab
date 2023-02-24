""" HowLong """

def main():
    """ find howlong of number"""
    num = abs(int(input()))
    howlong = 0
    for _ in str(num):
        howlong += 1
    print(howlong)
main()
