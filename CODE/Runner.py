""" This is Runner """


def runner():
    """ print text input times"""
    text = input()
    times = int(input())
    for i in range(0, times):
        if i != times:
            print(text)
        elif i == times:
            break
runner()
