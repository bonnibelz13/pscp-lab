""" PhoneNumber """

def main():
    """space 4 """
    num = input()
    nation = input()
    if len(num) == 9 and num[0] == "0":
        if nation == "Domestic":
            print(num[0]+" "+num[1:5]+" "+num[5:9]) #0 2123 4567
        elif nation == "International":
            print("+66"+" "+num[1:5]+" "+num[5:9])
    elif len(num) == 10 and num[0] == "0":
        if nation == "Domestic":
            print(num[0:2]+" "+num[2:6]+" "+num[6:10])
        elif nation == "International":
            print("+66"+num[1]+" "+num[2:6]+" "+num[6:10])

main()
