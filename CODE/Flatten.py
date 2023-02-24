''' Flatten '''
import json

def flatten(txt):
    ''' make list flatten '''
    flatlist = []
    if not isinstance(txt, list):
        flatlist.extend([txt])
    else:
        for i in txt:
            flatlist.extend(flatten(i))
    return flatlist
def main():
    ''' input '''
    txt = input()
    txt = json.loads(txt)
    flat = sorted(flatten(txt), reverse=True)
    print(flat)
main()
