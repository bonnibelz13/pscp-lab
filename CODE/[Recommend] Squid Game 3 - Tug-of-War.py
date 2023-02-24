""" [Recommend] Squid Game 3 - Tug-of-War """
def main():
    """ Tug of War """
    aaa = 0
    bbb = 0
    for i in range(1, 21):
        pull = int(input())
        if i < 11:
            aaa += pull
        else:
            bbb += pull
    if aaa > bbb:
        print('B')
    elif bbb > aaa:
        print('A')
    else:
        print('AB')
main()
