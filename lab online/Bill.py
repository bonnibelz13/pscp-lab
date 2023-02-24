""" Bill """


def main():
    """ service 10% and vat 7%"""
    num = int(input())
    service = num * 10/100
    total = 0
    if 1000 >= service >= 50:
        vat = (num + service) * 7/100
        total = vat + (num + service)
        print('%.2f' % total)
    elif service > 1000:
        service = 1000
        vat = (num + service) * 7/100
        total = vat + (num + service)
        print('%.2f' % total)
    elif service < 50:
        service = 50
        vat = (num + service) * 7/100
        total = vat + (num + service)
        print('%.2f' % total)


main()
