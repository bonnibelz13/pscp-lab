''' Kabata '''
def kabata():
    ''' kabata '''
    num = int(input())
    text = [input() for _ in range(num)]
    #print(text)
    newtext = [i.replace('baka', 'no').replace('bakka', '')\
        .replace('ka', '').replace('ba', '').replace('ta', '')\
            for i in text]
    for i in newtext:
        if i == '':
            #print(i)
            print('yes')
        else:
            #print(i)
            print('no')
kabata()
