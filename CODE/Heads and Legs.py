''' Heads and Legs '''
def findrandb():
    ''' find rabb and bird '''
    pet = int(input())
    all_legs = int(input())
    bird = (all_legs - (4 * pet))/-2
    rabb = pet - bird
    if rabb < 0 or bird < 0:
        print('Impossible')
    elif rabb - int(rabb) != 0 or bird - int(bird) != 0:    #check float หรือใช้ divmod ถ้าเหลือเศษ
        print('Impossible')
    else:
        print('%d %d' %(rabb, bird))
findrandb()
