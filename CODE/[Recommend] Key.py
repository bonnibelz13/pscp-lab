""" [Recommend] Key """
def main():
    """ sum 13 numbers, last3 x 10, sum13 with last3 """
    total = input()
    ksum = 0
    while (len(total) == 13) == True:
        for i in total:
            ksum += int(i)
        last = total[10:]
        total = str(ksum + (int(last)*10))
        num = int(total)
        if  num < 1000:
            num += 1000
            print(num)
        else:
            print(str(num)[-4:])
main()
