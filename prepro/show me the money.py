"""show me the money"""


def coin():
    """input"""
    pay = float(input())
    price = float(input())
    change = (pay - price)
    if change > 0:
        hundred = change // 100
        change = change % 100
        fifty = change // 50
        change = change % 50
        twenty = change // 20
        change = change % 20
        tweve = change // 12
        change = change % 12
        ten = change // 10
        change = change % 10
        five = change // 5
        change = change % 5
        two = change // 2
        change = change % 2
        one = change // 1
        change = change % 1
        fifcoin = change // 0.5
        change = change % 0.5
        twentyfive = change // 0.25
        change = change % 0.25

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
    elif change == 0:
        print("จ่ายมาพอดี")
    else:
        print("จำนวนเงินไม่พอ")


coin()
