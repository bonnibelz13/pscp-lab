""" Restaurant """
 
def main():
    """ """
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    if aaa > 0 and bbb >= aaa and 0 <= ccc <= 100 and ddd >= 0:
        dis = aaa + ddd
        if dis >= bbb:
            dis = dis*(ccc/100) - ddd
            if dis > 0:
                print('Yes %.3f'%abs(dis))
            elif dis == 0:
                print('Yes')
            elif dis < 0:
                print('No %.3f'%abs(dis))
    else:
        return
main()