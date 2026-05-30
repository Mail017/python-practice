message = input("Enter a message: ")
total = 0
for char in message:
    if char == "a":
        total += 1
    elif char == "e":
        total += 1
    elif char == "i":
        total += 1
    elif char == "o":
        total += 1
    elif char == "u":
        total += 1
print(f"Total number of vowels in the message: {total}")