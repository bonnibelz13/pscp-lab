class Time:
    """Represents the time of day."""
    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
    print_time(time=10)