"""This is everyday"""


def print_everyday():
    """I miss you everyday"""
    seconds = int(input())
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24

    time = "%02d:%02d:%02d:%02d" % (days, hours % 24, minutes % 60, seconds % 60)
    print(time)


print_everyday()
