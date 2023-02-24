''' LetterFrequency '''
def letterfrequen():
    ''' find the most used char in text '''
    txt = input().lower().replace(' ', '')
    print(max(set(txt), key=txt.count))
letterfrequen()
