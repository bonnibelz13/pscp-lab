"""Hamburger"""


def hamburger():
    """ความหนาของเนื้อ2หน่วยต่อขนมปัง1หน่วย"""
    left_bread = int(input())
    right_bread = int(input())
    left_meat = left_bread * 2
    right_meat = right_bread * 2
    print("|" * left_bread + "*" * left_meat + "*" * right_meat + "|" * right_bread)

hamburger()
