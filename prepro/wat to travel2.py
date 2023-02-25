"""Way to travel"""


def print_way():
    """way code"""
    weather = str(input())
    important = str(input())
    distance = float(input())
    if weather == "rainy" and important == "not important":
        print("Not go")
    elif weather == "rainy" and important == "important":
        if 0 < distance < 1:
            print("Walk")
        elif distance < 20:
            print("Motorcycle")
        elif distance < 300:
            print("Car")
        elif distance >= 300:
            print("Private Jet")
        elif distance < 0:
            print("Error")
    elif weather == "sunny":
        if important == "important" or important == "not important":
            if 0 < distance < 1:
                print("Walk")
            elif distance < 20:
                print("Motorcycle")
            elif distance < 300:
                print("Car")
            elif distance >= 300:
                print("Private Jet")
            elif distance < 0:
                print("Error")


print_way()
