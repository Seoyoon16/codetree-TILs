arr = list(map(int, input().split()))
cnt_arr = [0] * 10

for elem in arr:
    num = elem // 10
    cnt_arr[num] += 1

for i in range(1, 10):
    print(f"{i} - {cnt_arr[i]}")