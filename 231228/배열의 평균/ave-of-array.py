arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

arr_avg = []
for i in range(2):
    rsum = 0
    for j in range(4):
        rsum += arr_2d[i][j]
    ravg = rsum/4
    arr_avg.append(rsum/4)
    print(f"{ravg:.1f}", end=' ')
print()
for i in range(4):
    cavg = 0
    cavg = (arr_2d[0][i] + arr_2d[1][i]) / 2
    arr_avg.append(cavg)
    print(f"{cavg:.1f}", end=' ')
print()
asum = 0
for elem in arr_avg:
    asum += elem

print(f"{asum/6:.1f}")

# # 세로 평균
# for j in range(4):
# 	sum_val = 0
# 	for i in range(2):
# 		sum_val += arr_2d[i][j]