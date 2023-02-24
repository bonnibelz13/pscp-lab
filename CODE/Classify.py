''' Classify '''
def idstudent():
    ''' แสดงผลแยกชั้นปี และแยกคณะ '''
    dicttxt = []
    sameyear = []
    samefac = []
    while True:
        txt = input()
        if txt == 'END':
            break
        dicttxt.append(txt[:4])
        dicttxt = sorted(dicttxt)
    for i in dicttxt:
        year = i[:2]
        fac = int(i[2:4])
        if year != sameyear and fac != samefac:
            print(year, fac, dicttxt.count(i))
        elif year != sameyear and fac == samefac:
            print(year, fac, dicttxt.count(i))
        elif year == sameyear and fac != samefac:
            print('--', fac, dicttxt.count(i))
        elif year == sameyear and fac == samefac:
            continue
        sameyear = year
        samefac = fac
idstudent()
