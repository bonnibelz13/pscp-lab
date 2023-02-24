''' Coke V2 '''
def coke():
    ''' coke promotion '''
    oldprice = int(input())
    cap = int(input())
    proprice = int(input())
    want = int(input())

    while want >= 0:
        if cap == 0 or want == 0:
            print(oldprice * want)
            break
        else:
            total = (((oldprice * (cap-1)) + proprice) * ((want - 1)//cap)) +\
                ((((want - 1)%cap) * oldprice) + oldprice)
            print(total)
            break
coke()
