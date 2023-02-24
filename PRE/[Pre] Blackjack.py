"""This is Blackjack"""

"""
import math
def main():
    '''main'''
    days = int(input())
    arr_step = []
    for _ in range(days):
        arr_step.append((input()))
        arr_step = [w.replace('A', '100') for w in arr_step]
    print(arr_step)
    arr_step = [eval(i) for i in arr_step]
    avg = (sum(arr_step)/days)
    for i in arr_step:
        print(math.ceil(abs(i - avg)))
main()

"""
def main():

    num_card = int(input())
    mylist = []
    for _ in range(num_card):
        mylist.append(input().replace('A','1').replace('J','10').replace('K', '10').replace('Q', '10'))

    print(mylist)
    mylist = [eval(i) for i in mylist]
    print(mylist)
    if sum(mylist) < 21:
        mylist = [str(i) for i in mylist]
    print(mylist)
main()

# def main():
#     '''main'''
#     arr = []
#     while True:
#         char = input()
#         if char.upper() == "END":
#             break
#         arr.append(char)
#     num = int(input())
#     if num <= len(arr) - 1:
#         print('List[%d] = "%s"'%(num, arr[num]))
#     else:
#         print('Index Not Found')
# main()



# '''Append'''
# def main():
#     '''main'''
#     num = int(input())
#     arr = []
#     for _ in range(num):
#         arr.append('"%s"'%input())
#     print("[" + ", ".join(arr) + "]")
# main()
# Footer
# © 2022 GitHub, Inc.
# Footer navigation
# Terms







# def blackjack():
#     """ """
#     num_card = int(input())
#     deck = list('234567890JQKA').append(input())
#     value = {'2': 2, '3':3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
#                 '9': 9, '0': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
#     print(deck)
#
# blackjack()





# """This is Blackjack"""
#
#
# def main():
#     """print ค่าที่ดีที่สุด"""
#     num_card = int(input())
#     input_ = []
#     for v in range(num_card):
#         v = v + 1
#         input_.append(input())
#         input_ = ['1' if item == 'A' else item for item in input_]
#     print(input_)
#     input_ = [int(item) for item in input_]
#     print(input_)
#     print(sum(input_))
#     if sum(input_) < 21:
#         input_ = [str(item) for item in input_]
#         input_ = ['11' if item == '1' else item for item in input_]
#         print(input_)
#
#
# main()

"""
 def main():
     """"""

     num_card = int(input())
     mylist = []
     for _ in range(num_card):
         mylist.append(input())
         mylist = [w.replace('A', '1') for w in mylist]
     res = [eval(i) for i in mylist]
     print(res)
     if sum(res) < 21:
         res = [w.replace(1, 11) for w in res]
         print(res)
"""