"""Nearer"""


def main():
    """Nearer"""
    alice_x = int(input())
    bob_x = int(input())
    icecream = int(input())
    alice_1 = abs(icecream - alice_x)
    bob_2 = abs(icecream - bob_x)
    if alice_1 < bob_2:
        print("Alice", alice_1)
    elif alice_1 > bob_2:
        print("Bob", bob_2)
    else:
        print("Sundaes", bob_2)


main()
