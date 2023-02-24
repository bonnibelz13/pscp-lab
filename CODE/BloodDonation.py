''' BloodDonation '''
def blood():
    ''' blood donation check history '''
    age = int(input())
    weight = float(input())
    times = int(input())
    while True:
        if not 17 <= age <= 70:
            return 'No'
        if age == 17 or 60 <= age <= 70:
            book = input()
            if book == 'True':
                book = True
            elif book == 'False':
                book = False
        if weight < 45:
            return 'No'
        if times == 0 and age >= 55:
            return 'No'
        if age == 17 and book == False:
            return 'No'
        if 60 <= age <= 70 and book == False:
            return 'No'
        else:
            return 'Yes'
print(blood())
