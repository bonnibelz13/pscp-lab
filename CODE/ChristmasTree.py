""" ChristmasTree """
def main():
    """ print leave and stem """
    leave = int(input())
    stem = int(input())
    for i in range(1, leave + 1):
        print(' ' * (leave - i), end="")
        print('*' * (i + (i-1)))
    for _ in range(1, stem + 1):
        print(' ' * (leave - 2), end="")
        print('-' * 3, end="")
        print()
main()
