''' GCD_v1 and GCD_v2 '''
def gcd(numx, numy):
    ''' greatest common factor (หรม) '''
    while numy != 0:
        (numx, numy) = (numy, numx % numy)
    return numx
print(gcd(numx=int(input()), numy=int(input())))
