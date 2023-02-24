''' Meteorite '''
def main():
    ''' อุกกาบาต '''
    weight = float(input())
    meteorite = int(input())
    safeweight = float(input())
    if weight < safeweight:
        missile = 0
    else:
        devide = 0
        missile = 0
        while weight >= safeweight:
            weight = weight / meteorite
            missile += meteorite**devide
            devide += 1
    print(missile)
main()
