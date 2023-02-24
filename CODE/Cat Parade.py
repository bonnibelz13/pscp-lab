''' Cat Parade '''
def cat():
    ''' cat parade '''
    namecat = []
    while True:
        catinput = input().split(', ')
        namecat += catinput
        if catinput == ['IT\'S A DOG']:
            namecat.remove('IT\'S A DOG')
            namecat.remove(namecat[-1])
        if catinput == ['END']:
            namecat.remove('END')
            break
    sortnamecat = sorted(namecat)
    countedcat = []
    for i in range(len(sortnamecat)):
        if sortnamecat[i] not in countedcat:
            countedcat.append(sortnamecat[i])
    for i in range(len(countedcat)):
        countcat = sortnamecat.count(countedcat[i])
        print('%s %d %d' %(countedcat[i], (namecat.index(countedcat[i])+1), countcat))
cat()
