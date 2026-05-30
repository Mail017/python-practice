votes = ["Alice", "Bob", "Alice", "Mail", "Bob", "Alice", "Mail", "Alice"]
results = {}
for name in votes:
    if name in results:
        results[name] += 1
    else:
        results[name] = 1
for name, count in results.items():
    print(f"{name}: {count} votes")

print("ผู้ชนะคือ:", max(results, key=results.get))