"""This is Repeater"""

def repeater():
    """print text 100 times"""
    text = input()
    for _ in range(1, 101):
        print(text)
repeater()
