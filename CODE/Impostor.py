''' Impostor '''
import json
def impostor():
    ''' among us '''
    player = {}
    die = {}
    while True:
        txt = input()
        if txt == 'Start':
            continue
        if txt == 'End':
            break
        if txt[0] == '{':
            strtxt = json.loads(txt)
            player.update(strtxt)
        else:
            die.update({txt:player[txt]})

    #Alive players
    left = dict(set(player.items()) - set(die.items()))

    #All Impostors
    sus = 0
    for key in player:
        if player[key] == 'Impostor':
            sus += 1

    #Died Impostor
    diedimpostor = 0
    for key in die:
        if die[key] == 'Impostor':
            diedimpostor += 1

    #Output
    print('%d Impostor Remains'%(sus - diedimpostor))
    print('***Alive***')
    for i in sorted(left.items(), key=lambda x: x[0]):
        print(*i, sep=' : ')
    print('***Dead***')
    for i in sorted(die.items(), key=lambda x: x[0]):
        print(*i, sep=' : ')
impostor()
