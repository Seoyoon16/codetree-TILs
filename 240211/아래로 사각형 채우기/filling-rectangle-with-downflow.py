n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1; cnt = 0
for i in range(n):
    for j in range(n):
        arr[i][j] = num
        num += 5
    num = 1
    cnt += 1
    num += cnt

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()