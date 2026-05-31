## ฟังก์ชันสำหรับตรวจสอบและแยกส่วนของอีเมล
"""
def email(s):
    return s.split('@')[0]
input_email = input("ใส่ Email: ")
if '@' in input_email and '.' in input_email.split('@')[0] and input_email.split('@')[-1] != "@":
    print("Email ถูกต้อง ✓")
else:
    print("Email ไม่ถูกต้อง ✗")
"""
## เขียนโปรแกรมรับประโยคแล้วนับว่ามีกี่คำ
"""
word = input("ใส่ประโยค: ")
print(f"จำนวนคำในประโยค: {len(word.split())}")
print(f"คำที่ยาวที่สุด: {max(word.split(), key=len)}")
"""
## เขียนโปรแกรมตรวจสอบ Palindrome ไหม 🔄
"""
input_string = input("ใส่คำ: ")
if input_string == input_string[::-1]: ##กลับคำ เช่น "hello" → "olleh"
    print("เป็น Palindrome ✓")
else:
    print("ไม่เป็น Palindrome ✗")
"""
## เขียนโปรแกรมเข้ารหัสข้อความแบบง่ายๆ โดยเลื่อนตัวอักษรไป 3 ตัว (Caesar Cipher)
result = ""
message = input("ใส่ข้อความ: ")
for char in message:
    if char.isalpha(): ##ตรวจสอบว่าเป็นตัวอักษรหรือไม่
        result += chr(ord(char) + 3) ##เลื่อนตัวอักษรไป 3 ตัว
    else:
        result += char ##ถ้าไม่ใช่ตัวอักษรให้คงเดิม
print(f"ข้อความที่เข้ารหัส: {result}")