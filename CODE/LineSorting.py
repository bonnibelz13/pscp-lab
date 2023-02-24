''' LineSorting '''
def linesorting():
    ''' line and texts input เรียงบรรทัด สั้น ไป ยาว '''
    line = int(input())
    txt = [input() for _ in range(line)]
    sortedtxt = sorted(txt, key=len)
    print(*sortedtxt, sep='\n')
linesorting()
