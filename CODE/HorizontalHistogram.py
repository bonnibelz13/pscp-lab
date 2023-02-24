''' HorizontalHistogram '''
def histogram():
    ''' ความถี่อักษร ของข้อความที่ได้รับเข้ามา '''
    txt = input()
    dictword = dict()
    for word in txt:
        if word not in dictword:
            dictword[word] = 1
        else:
            dictword[word] = dictword[word] + 1
    #sorted(dictword, key=lambda x:(not x.islower(), x)))
    #newdict = {}
    #for text, val in dictword.items():
        #newdict.update({text: '-' * val})
    #newdict = sorted(newdict, key=lambda x:(not x.islower(), x))
    #for i in sorted(newdict.items(), key=lambda x: x[0].swapcase()):
        #print(*i, sep=' : ')
    print(dictword)
    for keys, vals in sorted(dictword.items(), key=lambda x: x[0].swapcase()):
        print(keys, ':', ''.join(['-' if i % 5 else '-|' for i in range(1, vals+1)]).rstrip('|'))
histogram()
