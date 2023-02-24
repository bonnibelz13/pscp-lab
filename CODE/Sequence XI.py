""" Sequence XI """

def square_top():
    """ square of number pattern top """
    num = int(input())
    for i in range(1, num+1): #i = rows แถว <-
        for j in range(1, num+1): #j = col หลัก ^
            if j >= i:
                print('%02d' %i, end=" ")
            elif j < i:
                print('%02d' %j, end=" ")
        for j in range(num-1, 0, -1):
            if j >= i:
                print('%02d' %i, end=" ")
            elif j < i:
                print('%02d' %j, end=" ")
        print()
    square_botom(num)
def square_botom(num):
    """ square of number pattern bottom """
    for i in range(num-1, 0, -1):
        for j in range(1, num+1):
            if j >= i:
                print('%02d' %i, end=" ")
            elif j < i:
                print('%02d' %j, end=" ")
        for j in range(num-1, 0, -1):
            if j >= i:
                print('%02d' %i, end=" ")
            elif j < i:
                print('%02d' %j, end=" ")
        print()
square_top()
