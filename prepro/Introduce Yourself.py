"""This is Introduce Yourself"""


def print_intro():
    """This is Introduce Yourself"""
    name = input()
    nickname = input()
    age = int(input())
    year = 2022 - age
    print("My name is", name + ", "
                               "My nickname is", nickname + ", "
                                                            "I'm I was born in", year)


print_intro()
