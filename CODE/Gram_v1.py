''' Gram_v1 '''
def gram():
    ''' WOWWOWO '''
    txt = input()
    txtlist = []
    wordlong = -1
    thatword = ''
    for i in range(len(txt) - 1):
        txtlist.append(txt[i] + txt[i+1])
    for i in txtlist:
        txtcount = txtlist.count(i)
        if txtcount > wordlong:
            wordlong = txtcount
            thatword = i
    print(thatword)
    print(wordlong)
gram()
