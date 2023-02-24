""" Run Length Decoding """
def main():
    """ Decode """
    txt = input()
    numtxt = 0
    txtout = ''
    num = ''
    while numtxt < len(txt):
        if txt[numtxt] in '1234567890':
            num += txt[numtxt]
            numtxt += 1
        else:
            txtout += txt[numtxt] * int(num)
            numtxt += 1
            num = ''
    print(txtout)
main()
