''' BreachTheDoor '''
import re
def password():
    ''' คำที่มีความยาวมากกว่า 6 ตัวอักษร เรียงจากต้นไปสุด '''
    txt = input()
    txt = txt.split('. ')
    #print(' '.join(k for k in txt if k.isalpha()))
    #print(txt)

    for i in range(len(txt)):
        word = txt[i].split()
        word = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in word]
        #print(' '.join(k for k in word if k.isalpha()))
        result = [j for j in word if len(j) > 6]
        if result == []:
            break
        else:
            print(*result, end=' ')
password()
