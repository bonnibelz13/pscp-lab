"""เรียงจากข้อความที่มีความยาวน้อยที่สุด ไปหาข้อความที่มีความยาวมากที่สุด"""


def dictionary_len():
    """เรียงข้อความจากความยาว"""
    txt1 = input()
    txt2 = input()
    txt3 = input()
    alltxt = [txt1.capitalize(), txt2.capitalize(), txt3.capitalize()]
    alltxt.sort(key=len)

    print(*alltxt, sep='\n')

dictionary_len()


#หรือ

def main():
    """ไม่ตอบ"""
    word1 = input().capitalize()
    word2 = input().capitalize()
    word3 = input().capitalize()
    new = sorted([word1, word2, word3], key=len)
    print("\n".join(new))
main()

#หรือ

"""เรียงข้อความ ยามเธออ่านไม่ตอบ"""


def main():
    """main func"""
    text = [input(), input(), input()]
    text.sort(key=len, reverse=False)
    print('%s\n%s\n%s' % (text[0].capitalize(), text[1].capitalize(), text[2].capitalize()))


main()