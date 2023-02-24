''' AlmostMean '''
def almostmean(score, mean):
    ''' score that near mean but not more than mean '''
    almostmeanscore = 0
    for i in sorted(score):
        if i >= almostmeanscore and i <= mean:
            almostmeanscore = i
    return almostmeanscore
def main():
    ''' line, idnumbers and scores input '''
    line = int(input())
    score = []
    listidnumber = [input().split('\t') for _ in range(line)]
    for i in range(0, line):
        score.append(float(listidnumber[i][1]))
    sumscore = sum(score)
    mean = sumscore / line
    indexthatscore = score.index(almostmean(score, mean))
    print('\t'.join(listidnumber[indexthatscore]))
main()
