''' CaesarV1 '''

def ceasar(num, txt):
    ''' Caesar Cipher การเลื่อน (Shift) ตัวอักษรตามจำนวน '''
    upper = {ascii:chr(ascii) for ascii in range(65, 91)}
    lower = {ascii:chr(ascii) for ascii in range(97, 123)}
    digit = {ascii:chr(ascii) for ascii in range(48, 58)}

    for i in txt:
        sym = ord(i)
        # ไม่ต้องเปลี่ยน sym หรือตัวเลข ใน txt
        if (sym not in upper and sym not in lower) or sym in digit:
            yield sym
        #char ใน txt
        else:
            # เลื่อนตัวพิมพ์ใหญ่ หรือ เลื่อนตัวพิมพ์เล็ก
            if sym in upper and sym + num % 26 in upper or sym in lower and sym + num % 26 in lower:
                yield sym + num % 26
            # เลื่อนกลับถ้าเป็นตัวอักษรตำแหน่งเกิน26
            else:
                yield sym + num % 26 -26

print((''.join(map(chr, ceasar(num=int(input()), txt=input())))))
