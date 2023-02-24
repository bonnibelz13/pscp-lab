''' Hamming '''
def ham():
    ''' Hamming Distance ของข้อความ 2 ข้อความที่รับเข้ามา '''
    txt1 = input()
    txt2 = input()
    numhamming = 0
    i = 0
    while i < len(txt1):
        if txt1[i] != txt2[i]:
            numhamming += 1
        i += 1
    print(numhamming)
ham()


# อีกวิธี
# '''PSCP Program'''
# def main(txt1, txt2, count):
#     '''8435-Hamming 18/11/2022'''
#     for i, j in enumerate(txt1):
#         count += 1 if j != txt2[i] else 0
#     print(count)
 
# main(input(), input(), 0)