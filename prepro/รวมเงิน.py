"""This is office"""


def print_company():
    """ print company """
    name_first = input()
    name_second = input()
    money_first = float(input())
    money_second = float(input())
    name_department = input()
    sep = input()

    money = (money_first + money_second)

    print(name_first + " " + name_second, money, name_department, sep=sep)

print_company()
