''' Muddled Menu '''
def menu():
    ''' course '''
    foodlist = []
    lastfood = []
    while True:
        food = input()
        foodlist.append(food.split(' #'))
        foodlistprint = [item[0] for item in foodlist]
        if food == 'DONE':
            foodlist.remove(['DONE'])
            foodlistprint.remove('DONE')
            break
        elif food[0:10:] == "Can't do: ":
            foodlistprint.remove(food[10::])
            foodlistprint.remove(food[0:])
            continue
        elif food == 'CLOSED':
            foodlist.clear()
            foodlistprint.clear()
            break
        elif food == 'SOMETHING\'S WRONG':
            foodlist.clear()
            foodlistprint.clear()
            continue
        else:
            if foodlist[-1].isnumberic():
                foodlist.
    print('Full Course: ',end='')
    print(foodlistprint)
    print('Reversed: ',end='')
    foodlistprint.reverse()
    print(foodlistprint)
menu()
