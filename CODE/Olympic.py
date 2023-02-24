''' Olympic '''
def olympic():
    ''' Scoreboard '''
    num = int(input())
    listwin = [input().split(' ') for _ in range(num)]
    dictwin = dict()
    for i in range(len(listwin)):
        dictwin.update({listwin[i][0]: listwin[i][1:4]})
    print(dictwin)
    newdictwin = {}
    for keys, val in dictwin.items():
        newdictwin.update({keys: sum([eval(i) for i in val])})
    print(sorted(newdictwin.items(),key=lambda x: x[1],reverse=True))
olympic()

'''
DOG 3 2 1
CAT 2 3 1
BAT 2 3 1
RAT 1 1 0
'''