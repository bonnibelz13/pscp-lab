"""BMIAgain"""


def main(weight, height):
    """bmi and rate"""
    if weight >= 0 and height >= 0:
        bmi = weight / (height * 0.01)**2
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        elif bmi >= 30:
            return "Obese"
    else:
        return
print(main(weight=int(input()), height=int(input())))
