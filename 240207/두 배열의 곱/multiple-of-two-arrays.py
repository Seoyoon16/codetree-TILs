# 첫 번째 2차원 배열을 구현해 정수를 입력받습니다.
arr_1 = [
	list(map(int, input().split()))
	for _ in range(3)
]
input() # 중간 한 줄 받기

# 두 번째 2차원 배열을 구현해 정수를 입력받습니다.
arr_2 = [
	list(map(int, input().split())) # [map(int, input().split())] 안됨
	for _ in range(3)
]

# print(arr_1)
# print()
# print(arr_2)

new_arr = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        new_arr[i][j] = arr_1[i][j] * arr_2[i][j]

# print(new_arr)

for row in new_arr:
    for elem in row:
        print(elem, end=' ')
    print()