"""
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    def introduce(self):
        get_grade = "A" if self.gpa >= 3.5 else "B" if self.gpa >= 2.0 else "C"
        print(f"สวัสดี ฉันชื่อ {self.name} GPA {self.gpa} เกรด {get_grade}")

s1 = Student("Mail", 2.85)
s1.introduce()
"""
## สร้าง Class BankAccount ที่จำลองบัญชีธนาคาร
"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"ฝากเงิน {amount} บาท --> ยอดคงเหลือ: {self.balance} บาท")
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"ถอนเงิน {amount} บาท --> เงินไม่พอ")
        else:
            self.balance -= amount 
            print(f"ถอนเงิน {amount} บาท --> ยอดคงเหลือ: {self.balance} บาท")

account = BankAccount("Mail", 1000)
print(f"เปิดบัญชี: {account.owner} ยอดเงิน: {account.balance} บาท")
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
print(f"ยอดเงินคงเหลือ: {account.balance} บาท")
"""
##สร้าง Class Employee แม่ และ Class ลูก 2 ตัว
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_info(self):
        print(f"{self.name} ทำงานและได้รับเงินเดือน {self.salary} บาท")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def get_info(self):
        print(f"Manager: {self.name} แผนก {self.department} ได้รับเงินเดือน {self.salary} บาท")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def get_info(self):
        print(f"Developer: {self.name} ภาษา {self.programming_language} และได้รับเงินเดือน {self.salary} บาท")

manager = Manager("Mail", 50000, "IT")
developer = Developer("Bob", 40000, "Python")
manager.get_info()
developer.get_info()
"""
## สร้าง Class สัตว์
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} กำลังกิน")
    def sleep(self):
        print(f"{self.name} กำลังนอน")
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.Color = color
    def meow(self):
        print(f"{self.name} เสียง meow!")
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(f"{self.name} เสียง โฮ่ง!")
dog = Dog ("บัดดี้", 5, "พันธุ์โกลเด้น")
cat = Cat ("วิสกี้", 3, "สีส้ม")
cat.eat()
cat.meow()
dog.sleep()
dog.bark()
print(f"{cat.name} {cat.Color} อายุ {cat.age} ปี")
print(f"{dog.name} {dog.breed} อายุ {dog.age} ปี")