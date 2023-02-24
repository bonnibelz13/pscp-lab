""" BootSequence """

def main():
    """ for loop number and sep='_', end='' """
    num = int(input())
    print(*[i for i in range(1, num+1)], sep='_')
main()
