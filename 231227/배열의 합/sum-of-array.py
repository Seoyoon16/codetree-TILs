# n = 4
# arr_2d = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]
# print(arr_2d)

arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

res = 0
for row in arr_2d:
    res = 0
    for col in row:
        res += col
    print(res)