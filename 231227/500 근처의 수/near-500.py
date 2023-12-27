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