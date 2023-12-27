n = int(input())
arr = list(map(int, input().split()))

for _ in range(n-1):
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
print(arr[-1], arr[-2])