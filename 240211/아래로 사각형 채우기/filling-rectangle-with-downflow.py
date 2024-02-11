n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1; cnt = 0
for i in range(n):
    for j in range(n):
        arr[i][j] = num
        num += n
    num = 1
    cnt += 1
    num += cnt

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()


# # 배열의 숫자를 채웁니다.
# for i in range(n):
# 	for j in range(n):
# 		arr[j][i] = num
# 		num += 1