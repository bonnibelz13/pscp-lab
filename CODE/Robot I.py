"""Robot I"""


def main(name, age):
    """name and age less than 18 pass"""
    if 0 < age < 18:
        print(name + ", " + "you can pass.")
    elif age >= 18:
        print(name + ", " + "you shall not pass.")
main(str(input()), float(input()))
