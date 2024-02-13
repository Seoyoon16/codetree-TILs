n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1
cnt = 0
for i in range(n-1, -1, -1):
    if cnt%2 == 0:
        for j in range(n):
            arr[n-1-j][i] = num
            num += 1
        cnt += 1
    else:
        for j in range(n):
            arr[j][i] = num
            num += 1
        cnt += 1

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()



# 4
# 33 23 13 03
# 02 12 22 32
# 31 21 11 01
# 00 10 20 30

# 5
# 44 34 24 14 04
# 03 13 23 33 43
# 42 32 22 12 02
# 01 11 21 31 41
# 40 30 20 10 00