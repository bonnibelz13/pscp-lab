''' Tuple's Sad life '''

def main():
    ''' Tuple's Sad life '''
    num = tuple(input().split())
    thatnum = input()
    position = num.index(thatnum)
    countthatnum = num.count(thatnum)
    for _ in range(countthatnum):
        out = str(position).split() * countthatnum
        print(*out)
main()
