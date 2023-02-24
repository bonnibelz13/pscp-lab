""" """
def loop(num):
    """ """
    while True:
        k = 0
        for i in str(num):
            k += int(i)
        if len(str(k)) == 1:
            break
        num = k
    return k
def main():
    """ """
    txt = input()
    while txt != '0':
        num = 0
        for i in txt:
            num += int(i)
        if num >= 10:
            print(loop(num))
        else:
            print(num)
        txt = input()
main()
