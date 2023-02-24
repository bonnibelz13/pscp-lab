""" test """
def main():
    """ scan o in txt """
    txt = input()
    virus = 0
    for _ in txt:
        if _ == 'o':
            virus += 1
    print(virus)
main()
