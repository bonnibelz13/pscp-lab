''' iPad Air '''
def ipad():
    ''' Choose ur iPad Air $$ '''
    color = input()
    capacity = int(input())
    spec = input()

    pay = 0
    listcolor = ['Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue']

    if color not in listcolor:
        print('Not Available')
        quit()

    if capacity == 64:
        pay += 19900
    elif capacity == 256:
        pay += 24900
    else:
        print('Not Available')
        quit()

    if spec == 'Wi-Fi':
        pay += 0
    elif spec == 'Wi-Fi + Cellular':
        pay += 4500
    else:
        print('Not Available')
        quit()
    print(pay)
ipad()
