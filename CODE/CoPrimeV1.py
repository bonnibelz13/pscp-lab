''' CoPrimeV1 '''
def gcd(numx, numy):
    ''' greatest common factor (หรม) '''
    while numy != 0:
        (numx, numy) = (numy, numx % numy)
    return numx

def main():
    ''' if prime of two input is 1 == YES else == NO '''
    numx = int(input())
    numy = int(input())
    if gcd(numx, numy) == 1:
        print('YES\n%d' %(gcd(numx, numy)))
    else:
        print('NO\n%d' %(gcd(numx, numy)))
main()
