""" [Recommend] Diginity """
def loop(num):
    """ loop sum mor than 10 """
    while True:
        count = 0
        for i in str(num):
            count += int(i)
        if len(str(count)) == 1:
            break
        num = count
    return count
def main():
    """ input txt """
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
