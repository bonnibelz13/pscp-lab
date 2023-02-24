''' BreachTheDoor '''
import re
def password():
    ''' คำที่มีความยาวมากกว่า 6 ตัวอักษร เรียงจากต้นไปสุด '''
    txt = input()
    txt = txt.split()
    txt = [re.sub('[^a-zA-Z]+', '', _) for _ in txt]
    print(*[a for i, a in enumerate(txt) if len(a) > 6])
password()
