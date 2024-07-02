n = int(input())
nums = [int(input()) for _ in range(n)]

total = sum(nums)
avg = round(total/n, 1)

print(total, avg)