""" test """
def grade(score):
    """ score to grade """
    if 95 <= score <= 100:
         return 'A'
    elif 90 <= score < 95:
        return 'B+'
    elif 85 <= score < 90:
        return 'B'
    elif 80 <= score < 85:
        return 'C+'
    elif 75 <= score < 85:
        return 'C'
    elif 70 <= score < 75:
        return 'D+'
    elif 65 <= score < 70:
        return 'D'
    elif 60 <= score < 65:
        return 'F+'
    elif 0 <= score < 60:
        return 'F'
def main():
    """ check 0 < score < 100 == True """
    score = float(input())
    if score < 0 or score > 100:
        print('ERR')
    else:
        print(grade(score) )
main()
