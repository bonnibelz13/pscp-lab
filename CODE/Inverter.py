''' Inverter '''
def inver():
    ''' ลองวิธีใหม่ๆ จ๊ '''
    txt = input()
    newtxt = ''
    for i in range(len(txt)):
        if txt[i] == '0':
            newtxt += '1'
        elif txt[i] == '1':
            newtxt += '0'
    print(newtxt.lstrip('0'))
inver()


# def inver():
#     ''' กลับ 0 เป็น 1 , 1 เป็น 0 ถ้า 0 อยุ่หน้าสุดตัดทิ้ง '''
#     txt = input()
#     newtxt = []
#     for i in range(len(txt)):
#         if txt[i] == '0':
#             newtxt.append('1')
#         elif txt[i] == '1':
#             newtxt.append('0')

#     #check newtxt[0] เป็น 0 ตัดทิ้ง
#     for i in range(len(newtxt)):
#         if newtxt[0] == '0':
#             newtxt.remove(newtxt[0])
#     print(*newtxt, sep='')
# inver()
