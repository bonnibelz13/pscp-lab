""" Run Length Encoding """
def main():
    """ encode """
    txt = input()
    txtout = ''
    count = 0
    numtxt = 0
    while numtxt < len(txt):
        if count == 0:
            start = txt[numtxt]
        if txt[numtxt] == start:
            count += 1
            numtxt += 1
        if numtxt == len(txt) or txt[numtxt] != start:
            txtout += '%d' % count + start
            count = 0
    print(txtout)
main()
