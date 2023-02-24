""" Restaurant """
def main():
    """ fix restaurant """
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    pay = aaa + ddd
    if pay >= bbb:
        pay = pay - (pay * (ccc/100))
    if aaa >= bbb:
        aaa = aaa - (aaa *(ccc/100))
    diff = abs(pay - aaa)
    if pay < aaa:
        print('Yes %.3f'%(diff))
    elif pay > aaa:
        print('No %.3f'%abs(diff))
    else:
        print('Yes')
main()
