''' Palindrome '''
def parin(num, txt):
    ''' อ่านจากหน้าไปหลัง หรือ อ่านจากหลังไปหน้า '''
    numed = 0
    while numed != num:
        natee = '%02d'%(int(txt[-2:]) + 1)
        hour = txt[0:2].replace(':', '')
        if int(natee) == 60 and int(natee) != 0:
            hour = int(hour) + 1
            natee = '00'
        if int(hour) >= 24:
            hour = 24-int(hour)
        txt = str(hour) + ':' + natee
        if txt.replace(':', '') == txt.replace(':', '')[::-1]:
            print(txt)
            numed += 1
parin(num=int(input()), txt=input())

#ติดเคส 10ตัว 23:59 ต้องได้ 0:00 ด้วย
