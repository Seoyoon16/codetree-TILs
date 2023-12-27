n = int(input())
arr = list(map(int, input().split()))

res = arr[1] - arr[0]
for i in range(1, n-1):
    if res >= arr[i+1] - arr[i]:
        res = arr[i+1] - arr[i]

print(res)