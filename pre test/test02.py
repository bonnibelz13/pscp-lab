p = True
q = False

a1 = p and q    # False ต้อง T และ T จะเป็น True ถ้ามี F จะเป็น False
a2 = p or q     # True ขอแค่ข้างใดข้างนึงเป็น T จะเป็น T
a3 = not p      # False สลับ
a4 = not q      # True

print( a1, a2, a3, a4 )