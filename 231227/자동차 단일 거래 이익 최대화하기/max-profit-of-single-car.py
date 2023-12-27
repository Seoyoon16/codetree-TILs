n = int(input())
arr = list(map(int, input().split()))

vmin = arr[0]
for i, elem in enumerate(arr):
    if elem <= vmin:
        vmin = elem
        idx = i

vmax = arr[idx]
for i, elem in enumerate(arr):
    if i >= idx:
        if elem >= vmax:
            vmax = elem

print(vmax-vmin)