"""BTS MRT"""
def main():
    """BTS MRT"""
    day = input()
    age = float(input())
    height = float(input())
    if day == "Children Day" and age < 14 and height <= 140\
        or (age < 14 and height < 90):
        print("FREE")
    elif day == "Senior Day" and age >= 60\
        or (age < 14 and height < 90):
        print("FREE")
    elif day == "Normal Day" and (age < 14 and height < 90):
        print("FREE")
    else:
        print("PAY")
main()
