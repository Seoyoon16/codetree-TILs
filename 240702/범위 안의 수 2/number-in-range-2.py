total = 0; number = 0
for _ in range(10):
    num = int(input())
    if num >= 0 and num <= 200:
        total += num
        number += 1

avg = round(total / number, 1)

print(total, avg)