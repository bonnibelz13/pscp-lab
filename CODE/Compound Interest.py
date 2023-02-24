''' Compound Interest '''
def compound_interest(money, rate, year):
    ''' cal compound interest '''
    amount = money
    for _ in range(year):
        amount += amount * rate
    return amount

def main():
    ''' input and print '''
    money = int(input())
    rate = float(input()) / 100
    year = int(input())
    print('%.2f' %compound_interest(money, rate, year))
main()
