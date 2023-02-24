''' Pro '''
def ejudge_pro():
    ''' promotion buffet '''
    proma = int(input())
    konpay = int(input())
    konla = int(input())
    magin = int(input())

    if magin >= proma:
        pay = ((magin//proma) * konpay) * konla
        leftma = (magin % proma) * konla
        pay += leftma
    else:
        pay = magin * konla
    print(pay)

ejudge_pro()
