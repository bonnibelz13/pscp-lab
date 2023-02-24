
""" test """
def main():
    ''' เงินเฟ้ออ '''
    pay = float(input())
    year = int(input())
    pay = int(pay * 100)
    for _ in range(year):
        expo = pay * 381
        pay = pay + expo//10000
    expo = str(pay)[-2:]
    pay = str(pay)[:-2]
    if pay == '':
        pay = '0'
    print('%d.%02d'%(int(pay), int(expo)))
main()
