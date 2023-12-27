# 초기값1 : max_val = -sys.maxsize
# 초기값2: max_val = arr[0]

arr = list(map(int, input().split()))

max_val = arr[0]
for elem in arr[1:]:
    if elem >= max_val:
        max_val = elem
    else:
        continue;

print(max_val)