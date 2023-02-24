""" """
def win(aaa, bbb):
    """ who win """
    if (aaa == 'R' and bbb == 'S') or (aaa == 'S' and bbb == 'P') or (aaa == 'P' and bbb == 'R'):
        return 'A'
    elif (bbb == 'R' and aaa == 'S') or (bbb == 'S' and aaa == 'P') or (bbb == 'P' and aaa == 'R'):
        return 'B'
    else:
        return ''
def main():
    """ """
    txt = input()
    txtwin = ''
    count_aaa = 0
    count_bbb = 0
    for i in range(len(txt)):
        if i %2 == 0:
            txtwin += win(txt[i], txt[i+1])
    for i in txtwin:
        if i == 'A':
            count_aaa += 1
        elif i == 'B':
            count_bbb += 1
    if count_aaa > count_bbb:
        print('A win %d - %d' %(count_aaa, count_bbb))
    elif count_bbb > count_aaa:
        print('B win %d - %d' %(count_bbb, count_aaa))
    else:
        print('DRAW %d' %count_aaa)
main()
