""" ValidVar """

def main():
    """ valid or invalid"""
    num = int(input())
    for i in range(num):
        text = input()
        firstnum = text[0]
        special_characters = "\"|][}{:;~'!@#$%^&*()-+?=,<>/.`"
        if any(i in " " for i in text[1:-1]) or any(i in special_characters for i in text) \
            or firstnum.isnumeric() or text == "if" or text == "else" or text == "elif" \
            or text == "while" or text == "for" or text == "True" or text == "False" \
            or text == "continue" or text == "break" or text == "return" \
            or text == "is" or text == "in" or text == "and" or text == "or" \
            or text == "from" or text == "as" or text == "pass" \
            or text == "not" or text == "def" or text == "None":
            print("Invalid")
        elif text[0] == " " or text[-1] == " ":
            print("Valid")
        else:
            print("Valid")
        i += 1
        if i == num:
            break

main()
