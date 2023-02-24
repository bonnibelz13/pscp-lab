''' WPM '''
def wpm_range():
    ''' range WPM '''
    age = input()
    wpm = int(input())
    if (age == 'Kids' and wpm < 11) or (age == 'Adults' and wpm < 26):
        print('Very Slow')
    elif age == 'Kids' and 11 <= wpm <= 20:
        print('Slow')
    elif age == 'Adults' and 26 <= wpm <= 35:
        print('Slow/Beginner')
    elif age == 'Kids' and 21 <= wpm <= 30:
        print('Average')
    elif age == 'Adults' and 36 <= wpm <= 45:
        print('Intermediate/Average')
    elif age == 'Kids' and 31 <= wpm <= 40:
        print('Fast')
    elif age == 'Adults' and 46 <= wpm <= 65:
        print('Fast/Advanced')
    elif (age == 'Kids' and wpm > 40) or (age == 'Adults' and 66 <= wpm <= 80):
        print('Very Fast')
    else:
        print('Insane')
wpm_range()
