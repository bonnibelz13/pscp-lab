""" Sequence IX """
 
def main():
    """ palindrome pyramid pattern """
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
main()