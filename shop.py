shop = {"ข้าว": 35, "น้ำเปล่า": 10, "ขนม": 15}

def show_menu():
    print("=== ร้านค้า ===")
    for name, price in shop.items():
        print(f"{name}: {price} บาท")

def calculate_total():
    total = 0
    while True:
        item = input("กรุณาเลือกสินค้า (พิมพ์ 'ออก' เพื่อจบ): ")
        if item == "ออก":
            break
        elif item in shop:
            num = int(input("กรุณาใส่จำนวน: "))
            print(f"รวม {num * shop[item]} บาท")
            total += num * shop[item]
        else:
            print("ไม่มีสินค้านี้!")
    return total

show_menu()
total = calculate_total()
print(f"ยอดรวมทั้งหมด: {total} บาท")