"""This is Sequence I"""


def loopnum(num, i, line):
    """ loop number """
    for i in range(0, num+1):
        if i != num:
            i += 1
            print(i, end=" ")
        elif i == num:
            line += 1
            if line == num:
                break
            elif line != num:
                i = 0
                print()
                loopnum(num, i, line)

def sequence(num, i, line):
    """ print num """
    loopnum(num, i, line)
sequence(num=int(input()), i=0, line=0)
