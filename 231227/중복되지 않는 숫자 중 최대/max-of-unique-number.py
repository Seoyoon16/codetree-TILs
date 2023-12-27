import sys

n = int(input())
arr = list(map(int, input().split()))

vmax = -sys.maxsize; vcheck = False
for i in range(n):
    cnt = arr.count(arr[i])
    if cnt == 1: 
        if arr[i] >= vmax:
            vmax = arr[i]
            vcheck = True
if vcheck == True:
    print(vmax)
else: print(-1)