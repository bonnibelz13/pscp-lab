""" [Recommend] iPhone 13 Again """
def gen_iphone(gen, capacity, pay):
    """ iPhone capacity """
    if capacity == '128 GB':
        pay += 0
    elif capacity == '256 GB':
        pay += 4000
    elif capacity == '512 GB':
        pay += 12000
    elif (gen == 'iPhone 13 Pro' and capacity == '1 TB') or\
        (gen == 'iPhone 13 Pro Max' and capacity == '1 TB'):
        pay += 20000
    else:
        pay = 'Not Available'
    return pay
def main():
    """ iPhone prices """
    gen = input()
    capacity = input()
    pay = 0
    if gen == 'iPhone 13 mini' or gen == 'iPhone 13' or gen == 'iPhone 13 Pro' or\
        gen == 'iPhone 13 Pro Max':
        if gen == 'iPhone 13 mini':
            pay += 25900
        elif gen == 'iPhone 13':
            pay += 29900
        elif gen == 'iPhone 13 Pro':
            pay += 38900
        elif gen == 'iPhone 13 Pro Max':
            pay += 42900
        print(gen_iphone(gen, capacity, pay))
    else:
        print('Not Available')
main()
