""" Milk """

def main():
    """ จะได้รับนมสูงสุดกี่ขวด """
    aaa = int(input())
    bbb = int(input())
    ccc = int(input())
    ddd = int(input())
    bot = ddd//aaa
    count = 0
    if bot//bbb >=1:
        for _ in range(bot):
            if bot//bbb >= 1:
                bot-=bbb
                bot+=ccc
                count+=ccc
            elif bot//bbb < 1:
                print((ddd//aaa)+count)
                break

main()
