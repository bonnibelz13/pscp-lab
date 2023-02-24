''' LastStand '''
import json

def main(txt):
    ''' LastStand '''
    newtxt = []
    for i in json.loads(txt):
        newtxt.append(str(i)[-1])
    print(*newtxt, sep='\n')
main(txt=input())
