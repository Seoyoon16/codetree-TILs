n = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]; cnt=0
for elem in arr[1:]:
    if elem < min_val:
        min_val = elem
        cnt = 1
    elif elem == min_val:
        cnt += 1
    else: pass;
if min_val == arr[0]:    # cnt를 애초에 1로 설정할 수도 있음
    cnt += 1

print(min_val, cnt)