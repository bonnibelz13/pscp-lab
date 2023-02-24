""" One For All """
def main():
    """ All might """
    num = int(input())
    oneforall = ''
    for i in range(1, num+1):
        name = input()
        if i %2 == 0 and i != num:
            oneforall += name + '-' * i
        elif i %2 != 0 and i != num:
            oneforall += name + '*' * i
        elif i == num:
            oneforall += name + '_' + str(num)
    print(oneforall)
main()
