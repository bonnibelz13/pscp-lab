''' Seeker '''
import re
def seeker():
    ''' find sum of numbers in the password '''
    txt = input()
    txt = re.findall(r'\d+', txt)
    txt = [int(i) for i in txt]
    print(sum(txt))
seeker()
