"""Way to travel"""


def print_way():
    """way code"""
    weather = str(input())
    main = str(input())
    distance = float(input())
    if distance < 0:
        print("Error")
    elif weather == "rainy" and main == "not important":
        print("Not go")
    elif weather == "rainy" and main == "important"\
            or weather == "sunny" and main == "important" or main == "not important":
        if distance < 1:
            print("Walk")
        elif distance < 20:
            print("Motorcycle")
        elif distance < 300:
            print("Car")
        elif distance >= 300:
            print("Private Jet")


print_way()
