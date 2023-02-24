''' B - Fully pair? '''
def pair():
    ''' จับคู่ลีลาศ '''
    txt = input()
    lll = [i for i in txt]
    nopair = []
    long = len(txt)
    j = 0
    while j < long:
        if lll.count(lll[j]) % 2 != 0 and lll[j] not in nopair:
            nopair.append(lll[j])
        j += 1
    if nopair == []:
        print('fully paired')
    else:
        print(*nopair, sep='')
pair()
