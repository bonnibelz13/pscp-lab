""" Lotto """
def lotto():
    ''' Lotto '''
    first = input()
    second = input()
    third = input()
    forth = input()
    fifth = input()
    sixth = input()
    lotory = input()
    result = 0
    if lotory == first:
        result += 6000000
    if lotory[-2:] == second:
        result += 2000
    if lotory[:3] == third and lotory[:3] == forth:
        result += 8000
    elif lotory[:3] == third or lotory[:3] == forth:
        result += 4000
    if lotory[-3:] == fifth and lotory[-3:] == sixth:
        result += 8000
    elif lotory[-3:] == fifth or lotory[-3:] == sixth:
        result += 4000
    if first == "000000" and (lotory == "999999" or lotory == "000001"):
        result += 100000
    elif first == "999999" and lotory == "000000":
        result += 100000
    elif int(first) - 1 == int(lotory) or int(first) + 1 == int(lotory):
        result += 100000
    else:
        result = result
    print(result)
lotto()
