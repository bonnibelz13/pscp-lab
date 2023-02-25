"""Profile Again"""


def main():
    """ข้อมูลลูกค้า เพศ รหัสไม่เกิน6หลัก ชื่อนามสกุลตัวแรกตัวใหญ่ อายุ อาชีพตัวใหญ่"""
    gender = str(input(["Female", "FEMALE", "Male", "MALE"]))
    code_id = input()
    name = input()
    surname = input()
    age = int(input())
    job = input()

    print("======")
    print("ID :", code_id[0:6])
    print("Name :", gender.replace("Mrs.", "Mr."), name.capitalize(), surname.capitalize())
    print("Age :", age, "years old")
    print("Occupation :", job.upper())
    print("======")
main()
