def main():
    """find unit of 7 exponent"""
    x = int(input())
    if x % 4 == 0:
        print("1")
    elif x % 4 == 1:
        print("7")
    elif x % 4 == 2:
        print("9")
    elif x % 4 == 3:
        print("3")
main()