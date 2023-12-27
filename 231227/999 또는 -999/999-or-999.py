arr = list(map(int, input().split()))

vmax = arr[0]; vmin = arr[0]
for elem in arr[1:]:
    if elem == 999 or elem == -999:
        break;
    
    if elem >= arr[0]:
        vmax = elem
    if elem <= arr[0]:
        vmin = elem
    
print(vmax, vmin)