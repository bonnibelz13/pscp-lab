''' BreakPassword '''
import hashlib

def breakpw():
    ''' break password '''
    txt = input()
    salt = 100000
    for i in range(salt):
        numintxt = str('%05d' %i)
        hashed = hashlib.sha512(numintxt.encode())
        password = str(hashed.hexdigest()).upper()
        if password == txt: #หาตัวเลขพาสที่เปนอันเดวกัน
            print('%05d' %i)
breakpw()
