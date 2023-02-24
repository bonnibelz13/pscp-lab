""" Parallelogram """

def main():
    """ <i> """
    text = input()
    long = len(text)
    for i in range(long):
        if i < long:
            for _ in range(1, long-i):
                print(" ", end="")
            for _ in range(i+1):
                print(text[_], end="")
            print()
    for i in range(long):
        if i < long:
            for _ in range(i+1, long):
                print(text[_], end="")
            print()

main()
