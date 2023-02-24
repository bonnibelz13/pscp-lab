""" Sequence XII """
def main():
    """ x """
    rows = int(input())
    for i in range(-rows + 1, rows):
        for j in range(-rows + 1, rows):
            print('%02d' %abs(rows - abs((abs(i) - abs(j)))), end=' ')
        print()
main()
