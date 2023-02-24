""" Calculator """
def cal():
    """ cal plus """
    num = int(input())
    txtnum = ''
    for i in range(1, num+1):
        if num == 1:
            txtnum += '1'
            break
        elif i == num:
            txtnum += str(i) + '='
        elif i < num:
            txtnum += str(i) + '+'
    print(len(txtnum))
cal()
