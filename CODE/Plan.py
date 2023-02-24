"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""


def plan(choose):
    """ Ascend """
    if choose == 'Ascend':
        num1, num2, num3 = float(input()), float(input()), float(input())
        if num1 <= num2 <= num3:
            print('%.2f, %.2f, %.2f'% (num1, num2, num3))
        elif num1 <= num3 <= num2:
            print('%.2f, %.2f, %.2f'% (num1, num3, num2))
        elif num2 <= num1 <= num3:
            print('%.2f, %.2f, %.2f'% (num2, num1, num3))
        elif num2 <= num3 <= num1:
            print('%.2f, %.2f, %.2f'% (num2, num3, num1))
        elif num3 <= num1 <= num2:
            print('%.2f, %.2f, %.2f'% (num3, num1, num2))
        elif num3 <= num2 <= num1:
            print('%.2f, %.2f, %.2f'% (num3, num2, num1))
    else:
        descend(choose)


def descend(choose):
    """ Descend """
    if choose == 'Descend':
        num1, num2, num3 = float(input()), float(input()), float(input())
        if num1 >= num2 >= num3:
            print('%.2f, %.2f, %.2f'% (num1, num2, num3))
        elif num1 >= num3 >= num2:
            print('%.2f, %.2f, %.2f'% (num1, num3, num2))
        elif num2 >= num1 >= num3:
            print('%.2f, %.2f, %.2f'% (num2, num1, num3))
        elif num2 >= num3 >= num1:
            print('%.2f, %.2f, %.2f'% (num2, num3, num1))
        elif num3 >= num1 >= num2:
            print('%.2f, %.2f, %.2f'% (num3, num1, num2))
        elif num3 >= num2 >= num1:
            print('%.2f, %.2f, %.2f'% (num3, num2, num1))

plan(choose=(input()))
