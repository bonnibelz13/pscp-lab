''' VerticalHistogram '''
def histogram():
    ''' ความถี่อักษร ของข้อความที่ได้รับเข้ามา but แนวตั้ง '''
    txt = input()
    #dictword = dict()
    #for word in txt:
    #    if word not in dictword:
    #        dictword[word] = 1
    #    else:
    #        dictword[word] = dictword[word] + 1
    #print(dictword)
    #print()

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dicttxt = {}
    for i in letters:
        dicttxt[i] = 0
        for char in txt:
            if char == i:
                dicttxt[i] += 1
    #print(dicttxt)

    mostword = dicttxt[max(dicttxt, key=dicttxt.get)]
    for count in range(mostword, 0, -1):
        print('%03d' %count, end='')
        for i in letters:
            if dicttxt[i] >= count and dicttxt[i] != 0:
                print(' *', end='')
            elif dicttxt[i] == 0:
                continue
            else:
                print('  ', end='')
        print()
    print(' ' * 3, end='')
    for i in letters:
        if dicttxt[i] > 0:
            print(' %s'%i, end='')
histogram()
