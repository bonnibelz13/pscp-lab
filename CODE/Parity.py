''' Parity '''

def main():
    ''' Parity '''
    num = input()
    txt = input()
    one = 0
    for i in num:
        if i == '1':
            one += 1
    if one % 2 != 0: #เป็นคี่
        if txt == 'Even':
            print(num + '1')
        elif txt == 'Odd':
            print(num + '0')
    else: #เป็นคู่
        if txt == 'Even':
            print(num + '0')
        elif txt == 'Odd':
            print(num + '1')
main()
