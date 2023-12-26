fst, sec = tuple(map(int, input().split()))

arr = [0] * 10
arr[0] = fst; arr[1] = sec
for i in range(2, 10):
    arr[i] = (arr[i-2]+arr[i-1])
    if arr[i] >= 10:
        arr[i] -= 10

for elem in arr:
    print(elem, end=' ')

# # 처음 두 수 입력
# p1, p2 = tuple(map(int, input().split()))
# arr = []

# # 앞의 두 수를 더한 값을 원소로 합니다.
# arr.append(p1)
# arr.append(p2)
# for i in range(2, 10):
# 	arr.append((arr[i - 2] + arr[i - 1]) % 10)
	
# # 10개의 정수를 출력
# for elem in arr:
# 	print(elem, end=" ")