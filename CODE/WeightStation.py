""" WeightStation """


def balance():
    """ balance overweight unbalance"""
    aver, wei1, wei2, wei3 = float(input()), float(input()), float(input()), float(input())
    leftwei = (aver*4) - (wei1 + wei2 + wei3)
    all_wei = wei1 + wei2 + wei3 + leftwei
    over = aver + (aver/2)
    under = aver - (aver/2)
    if all_wei > 15000:
        print("Overweight")
    elif all_wei <= 15000:
        if wei1 <= over and wei1 >= under \
            and wei2 <= over and wei2 >= under \
                and wei3 <= over and wei3 >= under \
                    and leftwei <= over and leftwei >= under:
            print("Pass", '%.2f' % leftwei)
        else:
            print("Unbalance")
balance()
