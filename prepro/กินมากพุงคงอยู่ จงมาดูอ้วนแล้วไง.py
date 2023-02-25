"""This is กินมากพุงคงอยู่ จงมาดูอ้วนแล้วไง"""


def print_bmi():
    """ Function BMI """
    name = input()
    weight = int(input())
    height = int(input())
    height_meter = height * 0.01
    bmi = weight / ((height_meter)**2)
    print("Name:", name)
    print("Weight:", weight, "kg.")
    print("Height: %.2f" % height_meter, "m.")
    print("BMI: %.2f" % bmi)


print_bmi()
