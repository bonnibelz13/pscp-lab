"""I N T E G E R"""


def print_num():
    data = (input())
    x = (input())
    if x == 2:
        print(bin(data))
    if x == 8:
        print(oct(data))
    if x == 10:
        print(dec)
    if x == 16:
        print(hex(data))


number= input('Enter a Binary number:')
dec_number= int(number, 2)
print('The decimal conversion is:', dec_number)
print(type(dec_number))
