''' Duplicate I '''
def dupli():
    ''' ชื่อซ้ำ '''
    numgroup_a = int(input())
    numgroup_b = int(input())
    name_a = set(input() for _ in range(numgroup_a))
    name_b = set(input() for _ in range(numgroup_b))
    same = sorted(name_a.intersection(name_b), reverse=True,)
    if same == []:
        print('Nope')
    else:
        for i in same:
            print(i)
dupli()
