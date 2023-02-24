''' Filter '''
import json
def filterscore():
    ''' print id : score that pass the filter '''
    txt = input()
    point = float(input())
    txt = json.loads(txt)
    idpass = {}
    for i in txt:
        if txt[i] >= point:
            idpass.update({i:txt[i]})
    idpass = dict(sorted(idpass.items()))
    for key in idpass.keys():
        idpass[key] = ('{:.2f}'.format(idpass[key]))
    for i in idpass.items():
        print(*i, sep='\t')
    if idpass == {}:
        print('Nope')

filterscore()
