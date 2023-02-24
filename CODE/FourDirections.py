""" FourDirections """
def direction():
    """ UDLR = up down left right  """
    direct = input()
    first = ''
    second = ''
    third = ''
    fourth = ''
    fifth = ''
    for i in direct:
        if i == 'U':
            first += '  *   '
            second += ' ***  '
            third += '* * * '
            fourth += '  *   '
            fifth += '  *   '
        elif i == 'D':
            first += '  *   '
            second += '  *   '
            third += '* * * '
            fourth += ' ***  '
            fifth += '  *   '
        elif i == 'L':
            first += '  *   '
            second += ' *    '
            third += '***** '
            fourth += ' *    '
            fifth += '  *   '
        elif i == 'R':
            first += '  *   '
            second += '   *  '
            third += '***** '
            fourth += '   *  '
            fifth += '  *   '
    print(first, second, third, fourth, fifth, sep='\n')
direction()
