arr_2d = [
    list(input().split())
    for _ in range(5)
]

for i in range(5):
    for j in range(3):
        # arr_2d[i][j] = chr(ord(arr_2d[i][j]) + ord('A') - ord('a'))
        arr_2d[i][j] = arr_2d[i][j].upper()
        # 바로 프린트 가능: print(arr_2d[i][j], end=" ")

for row in arr_2d:
    for col in row:
        print(col, end=' ')
    print()