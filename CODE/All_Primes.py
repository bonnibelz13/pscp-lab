''' All_Primes '''
def main():
    ''' check prime numbers '''
    nnn = int(input())
    countprime = 0
    listnum = []
    for i in range(1, nnn+1):
        listnum.append(i)
    for i in listnum:
        if i > 1:
            for _ in range(2, i):
                if (i % _) == 0:
                    break
            else:
                countprime += 1
    print(countprime)
main()
