""" Turnstile """
def main():
    """ Turnstile """
    action = input()
    gate = ''
    while action != 'END':
        if action == 'P':
            gate += action
        elif action == 'C':
            gate += action
        action = input()
    gate += action
    count = 0
    for i in range(len(gate)):
        if gate[i+1] == 'E':
            break
        elif gate[i] == 'C' and gate[i+1] == 'P':
            count += 1
        elif gate[i] == 'E':
            count = 0
            break
    print(count)
main()
