# # 1
# total = 0; number = 0
# for _ in range(10):
#     num = int(input())
#     if num >= 0 and num <= 200:
#         total += num
#         number += 1

# avg = round(total / number, 1)

# print(total, avg)

# 2
import statistics

numbers = [int(input()) for _ in range(10)]

for num in numbers:
    if num < 0 or num > 200:
        numbers.remove(num)

total = sum(numbers)
avg = round(statistics.mean(numbers), 1)

print(total, avg)