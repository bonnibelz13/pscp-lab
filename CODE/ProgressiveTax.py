""" ProgressiveTax """
def tax():
    ''' tax '''
    num = float(input())
    taxeiei = 0
    if num > 4000000:
        taxeiei += int((num - 4000000) * (35/100))
        num = 4000000
    if 2000000 < num <= 4000000:
        taxeiei += int((num - 2000000) * (30/100))
        num -= num - 2000000
    if 1000000 < num <= 2000000:
        taxeiei += int((num - 1000000) * (25/100))
        num -= num - 1000000
    if 750000 < num <= 1000000:
        taxeiei += int((num - 750000) * (20/100))
        num -= num - 750000
    if 500000 < num <= 750000:
        taxeiei += int((num - 500000) * (15/100))
        num -= num - 500000
    if 300000 < num <= 500000:
        taxeiei += int((num - 300000) * (10/100))
        num -= num - 300000
    if 150000 < num <= 300000:
        taxeiei += int((num - 150000) * (5/100))
        num -= num - 150000
    print(taxeiei)
tax()
