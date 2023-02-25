"""Choose a book"""


def way_to_choose_book():
    """function จัดหมวดหมู่่"""

    import math

    note = int(input())
    read = int(input())
    if note > 0 and read > 0:
        cal = math.factorial(note) / (math.factorial(read) * (math.factorial(note - read)))
        print(int(cal))

way_to_choose_book()
