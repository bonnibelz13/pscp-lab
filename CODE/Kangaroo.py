''' Kangaroo '''
def kanga(kanga_a, kanga_b, kanga_c):
    ''' max(c-b,b-a) - 1 '''
    return (max(kanga_c-kanga_b, kanga_b-kanga_a)) - 1
print(kanga(kanga_a=int(input()), kanga_b=int(input()), kanga_c=int(input())))
