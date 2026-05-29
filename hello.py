import random 

num = random.randint(1, 100)
count = 0

print("=== เกมทายตัวเลข ===")
while True:
    guess = int(input("ทายตัวเลข 1-100: "))
    count += 1

    if guess == num:
        print(f"ถูกต้อง! คุณทายได้ใน {count} ครั้ง")
        break
    elif guess < num:
        print("มากกว่า! ลองใหม่")
    else:
        print("น้อยไป! ลองใหม่")