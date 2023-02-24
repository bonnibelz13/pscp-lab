''' SMS '''
def sms():
    ''' ปุ่มกดโทรศัพท์มือถือ '''
    listbutton = [['A', 'B', 'C'], ['D', 'E', 'F'],\
        ['G', 'H', 'I'], ['J', 'K', 'L'],\
            ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],\
                ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

    num_button_press = int(input())
    txt = []

    for _ in range(num_button_press):
        button = int(input())
        times_press = int(input())
        if button == 1:
            for _ in range(times_press):
                txt.remove(txt[-1])
                if len(txt) == 0:
                    break
        if button == 2 or button == 3 or button == 4 \
            or button == 5 or button == 6 or \
                button == 8 and times_press > 0:
            if times_press % 3 == 0:
                txt.append(listbutton[button - 2][2])
            else:
                txt.append(listbutton[button - 2][(times_press % 3) - 1])
        if button == 7 or button == 9:
            if times_press % 4 == 0:
                txt.append(listbutton[button - 2][3])
            else:
                txt.append(listbutton[button - 2][(times_press % 4) - 1])
    if len(txt) <= 0:
        print('null')
    else:
        print(*txt, sep='')
sms()
