arr = list(map(int, input().split()))

arr1 = []; arr2 = []
for i in range(len(arr)):
    if arr[i] > 500:
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])

vmax = arr2[0]; vmin = arr1[0]    
for elem in arr1[1:]:
    if elem <= vmin:
        vmin = elem

for elem in arr2[1:]:
    if elem >= vmax:
        vmax = elem

print(vmax, vmin)


# # 배열에 정수를 입력받습니다.
# arr = list(map(int, input().split()))

# # max_val : 500 미만의 가장 큰 수, min_val : 500 초과의 가장 작은 수
# max_val = 1
# min_val = 1000
	
# # 10개의 숫자들 중 500근처의 수들을 구합니다.
# for elem in arr:
# 	if elem < 500 and elem > max_val:
# 		max_val = elem
		
# 	if elem > 500 and elem < min_val:
# 		min_val = elem
	
# # 구한 값을 출력합니다.
# print(max_val, min_val)