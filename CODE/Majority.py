''' Majority '''
def majority():
    ''' เลือกตั้งตึงๆ '''
    _ = int(input())
    people = int(input())
    listvote = [int(input()) for _ in range(1, people+1)]
    maxnum = max(listvote, key=listvote.count)
    if listvote.count(maxnum) > people / 2:
        print(maxnum, listvote.count(maxnum))
    else:
        print(0, listvote.count(maxnum))
majority()
