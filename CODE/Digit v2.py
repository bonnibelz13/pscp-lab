''' Digit v2 '''
def digit():
    ''' แปลงจากตัวเลขเป็นคำอ่านภาษาอังกฤษให้หน่อย '''
    txt = input()
    dicttxt = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        }

    total = []
    for num in txt.split(' '):
        if num in dicttxt:
            total.append(dicttxt[num])
        elif num == 'hundred':
            total[-1] *= 100
        elif num == 'thousand':
            total = [x * 1000 for x in total]

    #print(sum(total))  ดูเลข
    print(len(str(sum(total))))

digit()
