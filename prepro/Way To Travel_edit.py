"""Way To Travel eiei"""


def gogo():
    """อากาศดีมั้ยคะไอ้ต้าว"""
    weather = str(input())
    lesgo = str(input())
    dis = float(input())
    if weather == "rainy":
        if lesgo == "not important":
            print("Not go")
        elif lesgo == "important":
            if 0 < dis < 1:
                print("Walk")
            elif 1 < dis < 20:
                print("Motorcycle")
            elif 20 < dis < 300:
                print("Car")
            elif dis >= 300:
                print("Private Jet")
            elif dis < 0:
                print("Error")
    if weather == "sunny":
        if lesgo == "important" or lesgo == "not important":
            if 0 < dis < 1:
                print("Walk")
            elif 1 < dis < 20:
                print("Motorcycle")
            elif 20 < dis < 300:
                print("Car")
            elif dis >= 300:
                print("Private Jet")
            elif dis < 0:
                print("Error")

gogo()
