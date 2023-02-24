def check(num):
    ''' check i is Perfect numbers'''
    return [(2**p - 1) * (2**(p - 1)) for p in mersenne_prime_powers[:num]]
def main():
    ''' input and print '''
    num = int(input())
    print(check(num))
mersenne_prime_powers = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]
main()
