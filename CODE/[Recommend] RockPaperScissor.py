""" [Recommend] RockPaperScissor """

def check(py1, py2):
    """ find who win"""
    ans = ''
    if (py1 == 'R' and py2 == 'S') or (py1 == 'S' and py2 == 'P') or (py1 == 'P' and py2 == 'R'):
        ans = 'A'
    elif (py2 == 'R' and py1 == 'S') or (py2 == 'S' and py1 == 'P') or (py2 == 'P' and py1 == 'R'):
        ans = 'B'
    elif py1 == py2:
        pass
    return ans
def main():
    """ start the game RPS """
    game = input()
    whowin = ''
    for i in range(len(game)):
        if i % 2 == 0:
            whowin += check(game[i], game[i+1])
    apoint = whowin.count('A')
    bpoint = whowin.count('B')
    if apoint > bpoint:
        print('A win %d-%d' %(apoint, bpoint))
    elif bpoint > apoint:
        print('B win %d-%d' %(bpoint, apoint))
    else:
        print('DRAW %d' %apoint)
main()
