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
'''
리스트를 순회하면서 원소를 삭제할 때는,
1) 새로운 리스트를 생성
2) 인덱스를 역순으로 순회하며 삭제

'''
filtered_numbers = [num for num in numbers if 0 <= num <= 200]

total = sum(filtered_numbers)
avg = statistics.mean(filtered_numbers)

print(total, f"{avg:.1f}")