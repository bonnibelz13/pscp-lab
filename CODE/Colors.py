''' Colors '''
def colors():
    ''' นำแม่สีมาผสมกัน '''
    xxx = input()
    yyy = input()
    listcolor = ['Red', 'Yellow', 'Blue']
    if xxx not in listcolor or yyy not in listcolor:
        print('Error')
        quit()
    if xxx == yyy:
        print(xxx)
    if (xxx == 'Red' and yyy == 'Yellow') or (yyy == 'Red' and xxx == 'Yellow'):
        print('Orange')
    if (xxx == 'Red' and yyy == 'Blue') or (yyy == 'Red' and xxx == 'Blue'):
        print('Violet')
    if (xxx == 'Yellow' and yyy == 'Blue') or (yyy == 'Yellow' and xxx == 'Blue'):
        print('Green')
colors()
