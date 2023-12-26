fst, sec = tuple(map(int, input().split()))

arr = [0] * 10
arr[0] = fst; arr[1] = sec
for i in range(2, len(arr)):
    arr[i] = arr[i-1] + 2*arr[i-2]

for elem in arr:
    print(elem, end=' ')