# n X m 2차원 배열 초기화
# arr_2d = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]

n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

k = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = k
        k += 1

for row in arr:
    for col in row:
        print(col, end=' ')
    print()