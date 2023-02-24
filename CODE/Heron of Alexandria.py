""" Heron of Alexandria """
import math

def heron():
    """ Heron of Alexandria """
    numa = float(input())
    numb = float(input())
    numc = float(input())
    s_area = (numa + numb + numc)/2
    area = math.sqrt(s_area*(s_area - numa)*(s_area - numb)*(s_area - numc))
    print('%.3f'%area)
heron()
