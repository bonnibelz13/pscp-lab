""" This is BrickBridge"""
def brick():
    """ find use_brick_a """
    numa = int(input())
    numb = int(input())
    goal = int(input())
    wantb = goal//5
    useb = min(wantb, numb)
    usea = goal - useb*5
    if usea <= numa:
        print(usea)
    else:
        print(-1)
brick()
