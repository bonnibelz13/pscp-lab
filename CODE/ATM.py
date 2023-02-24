''' ATM '''
def atm():
    ''' กดฝาก ถอน ไปเรื่อยๆ จงหาว่าสุดท้ายแล้วเหลือเงินเท่าใด '''
    money = int(input())
    while True:
        act = input()
        if act[0] == 'D':
            money += int(act[2:])
        elif act[0] == 'W' and int(act[2:]) >= money:
            money = 0
        elif act[0] == 'W':
            money -= int(act[2:])
        elif act == 'END':
            break
    print(money)
atm()
