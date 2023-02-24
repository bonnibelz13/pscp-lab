''' Roman '''
def roman_to_number(txt):
    ''' Roman to number '''
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(txt)):
        if i > 0 and roman[txt[i]] > roman[txt[i - 1]]:
            num += roman[txt[i]] - 2 * roman[txt[i - 1]]
        else:
            num += roman[txt[i]]
    return num
print(roman_to_number(txt=input()))
