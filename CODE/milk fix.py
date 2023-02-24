""" Milk """
def milk():
    ''' free milk '''
    price = int(input())
    free = int(input())
    bottle = int(input())
    pay = int(input())
    num_bot = pay//price
    num_free = num_bot
    while num_free >= free and free > 0:
        first = (num_free//free)* bottle
        second = num_free % free
        num_bot += first
        num_free = first + second
    print(num_bot)
milk()
