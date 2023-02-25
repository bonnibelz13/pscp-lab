"""BMI Upgrade"""


def bmi_find():
    """ติ่งแหน๊ด"""
    weight = float(input())
    height = float(input())
    age = int(input())
    bmi = weight / (height*0.01)**2
    if age < 18:
        print("Please use BMI for Children and Teens.")
    elif bmi < 16:
        print("Severe Thinness")
    elif 16 <= bmi <= 16.99:
        print("Moderate Thinness")
    elif 17 <= bmi <= 18.49:
        print("Mild Thinness")
    elif 18.5 <= bmi <= 24.99:
        print("Normal")
    elif 25 <= bmi <= 29.99:
        print("Overweight")
    elif 30 <= bmi <= 34.99:
        print("Obese lass I")
    elif 35 <= bmi <= 39.99:
        print("Obese lass II")
    elif bmi >= 40:
        print("Obese lass III")


bmi_find()
