
def main():
    ''' line, idnumbers and scores input '''
    line = int(input())
    score = []
    listidnumber = [input().split('\t') for _ in range(line)]
    for i in range(0, line):
        score.append((listidnumber[i][1]))

main()