''' 3nPlus1 '''
def three_n_plus_one():
    ''' 3n + 1 Problem '''
    while True:
        num = int(input())
        listnum = []
        while num != 1:
            listnum.append(num)
            if num == 0:
                quit()
            if num % 2 == 0:
                num = num / 2
            else:
                num = (3 * num) + 1
        print(len(listnum)+1)
three_n_plus_one()
