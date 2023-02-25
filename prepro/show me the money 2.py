"""show me the money"""


def coin():
    """input"""
    pay = float(input())
    price = float(input())
    change = (pay - price)
    if change > 0:
        hundred = change // 10000
        change = change % 10000
        fifty = change // 5000
        change = change % 5000
        twenty = change // 2000
        change = change % 2000
        tweve = change // 1200
        change = change % 1200
        ten = change // 1000
        change = change % 1000
        five = change // 500
        change = change % 500
        two = change // 200
        change = change % 200
        one = change // 100
        change = change % 100
        fifcoin = change // 50
        change = change % 50
        twentyfive = change // 25
        change = change % 25

        print("เเบงค์ 100 บาท :", int(hundred))
        print("เเบงค์ 50 บาท :", int(fifty))
        print("เเบงค์ 20 บาท :", int(twenty))
        print("เหรียญ 12 บาท :", int(tweve))
        print("เหรียญ 10 บาท :", int(ten))
        print("เหรียญ 5 บาท :", int(five))
        print("เหรียญ 2 บาท :", int(two))
        print("เหรียญ 1 บาท :", int(one))
        print("เหรียญ 50 สตางค์ :", int(fifcoin))
        print("เหรียญ 25 สตางค์ :", int(twentyfive))
        print("change =", change)
    elif change == 0:
        print("จ่ายมาพอดี")
    else:
        print("จำนวนเงินไม่พอ")

coin()
