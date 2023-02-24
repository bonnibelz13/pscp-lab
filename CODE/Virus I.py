""" Virus I"""


def main():
    """ scan o in text """
    text = input()
    num = 0
    for _ in text:
        if _ == 'o':
            num += 1
    print(num)


main()
