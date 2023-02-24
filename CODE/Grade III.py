""" Grade III"""


def grade(num):
    """2"""
    grade_score = 0
    if num >= 95 and num <= 100:
        grade_score = 4
    elif num < 95 and num >= 90:
        grade_score = 3.5
    elif num < 90 and num >= 85:
        grade_score = 3
    elif num < 85 and num >= 80:
        grade_score = 2.5
    elif num < 80 and num >= 75:
        grade_score = 2
    elif num < 75 and num >= 70:
        grade_score = 1.5
    elif num < 70 and num >= 65:
        grade_score = 1
    elif num < 65 and num >= 60:
        grade_score = 0.5
    elif num < 60 and num >= 0:
        grade_score = 0
    return grade_score


def main(subject):
    """Main Function"""
    count = 0
    total = 0
    while count < subject and subject > 0:
        score = float(input())
        total += grade(score)
        count += 1
    print("%.2f" % ((int((total/count)*100))/100))


main(int(input()))
