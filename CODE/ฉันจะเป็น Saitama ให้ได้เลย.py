""" ฉันจะเป็น Saitama ให้ได้เลย """
import math


def saitama():
    ''' how to be saitama '''
    vid = int(input())
    sit = int(input())
    stand = int(input())
    run = int(input())
    dovid = int(input())
    dosit = int(input())
    dorun = int(input())
    dostand = int(input())
    dayv = math.ceil(vid/dovid)
    daysi = math.ceil(sit/dosit)
    dayst = math.ceil(stand/dostand)
    dayr = math.ceil(run/dorun)
    day = dayv
    if daysi >= day:
        day = daysi
    if dayst >= day:
        day = dayst
    if dayr >= day:
        day = dayr
    print('%d'%day)
saitama()
