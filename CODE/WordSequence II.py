''' WordSequence II '''
def wordsequence():
    ''' convert/transform the start text to last text '''
    starttxt = input()
    lasttxt = input()
    for i in range(max(len(starttxt), len(lasttxt))+1):
        print(lasttxt[:i] + starttxt[i:])
wordsequence()
