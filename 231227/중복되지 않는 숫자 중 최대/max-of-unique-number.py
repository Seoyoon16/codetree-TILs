n = int(input())
arr = list(map(int, input().split()))

vmax = arr[0]; success = True
for elem in arr[1:]:
    if elem >= vmax:
        vmax = elem
        arr.remove(elem)
        if elem in arr:
            vmax = arr[0]
            arr.append(elem)
        else:
            print(vmax)
            success = False

if success == True:
    print(-1)