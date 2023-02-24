''' WordSequence I '''
def wordsequence():
    ''' print char+n '''
    starttxt = input()
    lasttxt = input()
    for i in range(max(len(starttxt), len(lasttxt))):
        print(lasttxt[:i] + starttxt[i:])
wordsequence()
