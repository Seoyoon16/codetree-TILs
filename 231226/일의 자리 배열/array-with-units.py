fst, sec = tuple(map(int, input().split()))

arr = [0] * 10
arr[0] = fst; arr[1] = sec
for i in range(2, 10):
    arr[i] = (arr[i-2]+arr[i-1])
    if arr[i] >= 10:
        arr[i] -= 10

for elem in arr:
    print(elem, end=' ')