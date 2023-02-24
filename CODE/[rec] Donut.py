""" test """
def main():
    """ find pay and pieces of donut that we get """
    price = int(input())
    buythis = int(input())
    getthis = int(input())
    wantdonut = int(input())
    free = buythis + getthis #ซื้อโดนัทถึงเท่า buythis ชิ้น แถม getthis ชิ้น รวมโปรโมชั่นนี้จะได้เป็น free ชิ้น 
    promotion = price * buythis #ราคาโปรโมชั่น
    times = wantdonut // free #จำนวนครั้งที่ได้โปรโมชั่น เอาโดนัทที่ต้องการ // โดนัทที่ได้ในโปรโมชั่น จะได้จำนวนครั้งที่ซื้อโปรโมชั่น
    leftdonut = wantdonut - (times * free) #หาจำนวนโดนัทที่ขาดไป
    if leftdonut >= buythis: #ถ้าโดนัทที่เหลือมันมากกว่าที่แถม งั้นก็ซื้อโปรโมชั่นไปอีกครั้งเลย (ทีนี้จะได้จำนวนโดนัทเกินกว่าที่เราอยากได้แล้ว)
        times += 1
        leftdonut = 0 #โดนัทเกินกว่าที่ต้องการแล้ว เลยให้ leftdonut = 0
    pay = (times * promotion) + (leftdonut * price) #อย่าลืม x ด้วยจำนวนโดนัทที่ขาด กรณีที่จำนวนโดนัทต้องการที่ขาดไม่ถึงจำนวนโปรโมชั่น
    getdonut = (times * free) + leftdonut
    print(pay, getdonut)
main()
