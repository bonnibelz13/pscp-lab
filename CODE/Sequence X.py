""" Sequence X """

def main():
    """ diamond pattern """
    num = int(input())
    if 0 < num < 100:
        for i in range(1, num+1):
            for k in range(1, num-i+1):
                print(" ", end="  ")
            for k in range(1, i+1):
                print('%02d'%k, end=" ")
            for k in range(k-1, 0, -1):
                print('%02d'%k, end=" ")
            print()
        for i in range(num+1, 2, -1):
            for j in range(1, num-i+3):
                print(" ", end="  ")
            for j in range(k, i-1):
                print('%02d'%j, end=" ")
            for j in range(i-3, 0, -1):
                print('%02d'%j, end=" ")
            print()
main()
