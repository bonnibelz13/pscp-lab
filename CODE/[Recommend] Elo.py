""" [Recommend] Elo """
def main():
    """ cal Elo rating """
    rta = int(input())
    rtb = int(input())
    elo = input()
    if rta >= 0 and rtb >= 0:
        eloa = 1 / (1 + (10**((rtb - rta) / 400)))
        elob = 1 / (1 + (10**((rta - rtb) / 400)))
    while eloa + elob == 1:
        if elo == 'A':
            print('%.2f'%eloa)
        elif elo == 'B':
            print('%.2f'%elob)
        break
main()
