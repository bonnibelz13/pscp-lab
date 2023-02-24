''' RemoveTag '''
def removetag(text):
    ''' remove html '''
    symbb = ''
    txt = []
    istxt = True
    if '<' in text:
        for i in text:
            if i == '<':
                istxt = False
                symbb = symbb.split()
                txt.extend(symbb)
                symbb = ''
            elif i == '>':
                istxt = True
            elif istxt:
                symbb += i
        print(txt)
    else:
        txt = text.split()
        print(txt)
removetag(text=input())
