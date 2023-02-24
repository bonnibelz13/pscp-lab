""" Donut fix """

def main():
    """ แถมแถม """
    abaht = int(input())
    bpiece = int(input())
    cpiece = int(input())
    wantd = int(input())
    free = bpiece + cpiece
    bahtfree = abaht * bpiece
    times = wantd//free
    donut = wantd - (times*free)
    if donut >= bpiece:
        times += 1
        donut = 0
    print(times*bahtfree + donut*abaht, times*free + donut)
main()
