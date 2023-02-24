""" test """
def main():
    """ Hamburger """
    lbread = int(input())
    rbread = int(input())
    print('|' * lbread + '*' * (2 * (lbread + rbread)) + '|' * rbread)
main()
