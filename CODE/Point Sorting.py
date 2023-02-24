''' Point Sorting '''
#เรียงจุดเหล่านี้ตามค่าจากฟังก์ชัน f ที่นิยามว่า f(x,y) = x + y จากน้อยไปมาก
#ถ้ามีจุดที่มีค่าฟังก์ชัน f เท่ากัน ให้เรียงโดยให้จุดที่มีค่าพิกัดบนแกน y มากกว่ามาก่อน
def pointtosort(point):
    ''' return point that sorted '''
    return int(point[0]) + int(point[1]), -int(point[1])
def main():
    ''' input test times and numbers '''
    test = int(input())
    numlist = []
    for _ in range(test):
        lastnum = int(input())
        for _ in range(lastnum):
            numpoint = input().split()
            numlist.append(numpoint)
        numlist.sort(key=pointtosort)
        #print(numlist)
        for i in numlist:
            print(*i)
        numlist.clear()
main()
