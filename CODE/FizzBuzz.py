""" FizzBuzz """

def main(num):
    """ Main Function """
    if num > 0:
        for _ in range(1, num+1):
            if _ % 3 == 0 and _ % 5 == 0:
                print("FizzBuzz")
            elif _ % 3 == 0:
                print("Fizz")
            elif _ % 5 == 0:
                print("Buzz")
            else:
                print(_)

main(int(input()))
