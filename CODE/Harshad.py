""" Harshad """
def main():
    ''' idk '''
    i = 0
    while i < 10:
        num = int(input())
        num = abs(num)
        num2 = num
        if len(str(num)) == 1 and num != 0:
            print("Yes")
        elif len(str(num)) > 1:
            total = 0
            for j in str(num):
                total += int(j)
            num = total
            if num2 % num == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
        i += 1
main()
