''' Muddled Menu '''
def menu():
    ''' course foodlist foodnum '''
    foodlist = []
    while True:
        food = input()
        if food == 'DONE':
            break
        if food == 'SOMETHING\'S WRONG':
            foodlist.clear()
            continue
        if food[0:10] == 'Can\'t do: ':
            foodlist.remove(food[10:])
        if food == 'CLOSED':
            foodlist.clear()
            break
        else:
            foodnum = food.split(' #')
            if food[-1].isalpha() and foodnum[0][0:10] != 'Can\'t do: ':
                foodlist.append(foodnum[0])
            elif foodnum[0][0:10] == 'Can\'t do: ':
                continue
            elif foodnum[1].isnumeric():
                foodlist.insert(int(foodnum[1])-1, foodnum[0])
    print('Full Course: ', end='')
    print(foodlist, end=' ')
    foodlist.reverse()
    print('Reversed: ', end='')
    print(foodlist)
menu()
