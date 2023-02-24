''' BookWorm '''
def book():
    ''' sum reading time that in time '''
    testtimes = int(input())
    for _ in range(testtimes):
        minute = float(input())
        books = int(input())
        timeofbook = [float(input()) for _ in range(books)]
        timeofbook = sorted(timeofbook)
        i = 0
        for i in range(len(timeofbook)):
            if sum(timeofbook[:i+1]) > minute:
                break
            i += 1
        print(i)
book()
