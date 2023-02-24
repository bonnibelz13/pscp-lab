"""BigFrame"""
def main():
    """BigFrame"""
    text_1 = input().strip()
    text_2 = input().strip()
    text_3 = input().strip()
    text_4 = input().strip()
    text_5 = input().strip()
    longest = max(len(text_1), len(text_2), len(text_3), len(text_4), len(text_5))
    print("**" + "*"*longest + "**")
    print("* " + text_1 + " "*(int(longest-int(len(text_1)))) + " *")
    print("* " + text_2 + " "*(int(longest-int(len(text_2)))) + " *")
    print("* " + text_3 + " "*(int(longest-int(len(text_3)))) + " *")
    print("* " + text_4 + " "*(int(longest-int(len(text_4)))) + " *")
    print("* " + text_5 + " "*(int(longest-int(len(text_5)))) + " *")
    print("**" + "*"*longest + "**")
main()
