"""Timing"""


def main(time):
    """second to day hour minute second"""
    if time > 863999999:
        return "ERR_:__:__:__"
    else:
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        return "%04d:%02d:%02d:%02d" % (day, hour, minutes, seconds)
print(main(time=float(input())))
