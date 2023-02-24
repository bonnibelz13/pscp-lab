''' Password '''
import hashlib
def password():
    ''' แปลงข้อความรหัสผ่านใดๆ ผ่าน SHA512 Encoding ใช้ UTF-8'''
    txt = input()
    res = hashlib.sha512(txt.encode()).hexdigest().upper()
    print(res)
password()
