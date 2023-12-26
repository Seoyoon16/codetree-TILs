arr = []
for _ in range(3):
    person = list(input().split())
    arr.append(person)

cnt_arr = [0] * 4

cnt = 0
for i in range(len(arr)):
    arr[i][1] = int(arr[i][1])
    if arr[i][0] == 'Y' and arr[i][1] >= 37:
            cnt_arr[0] += 1
    elif arr[i][0] == 'N' and arr[i][1] >= 37:
        cnt_arr[1] += 1
    elif arr[i][0] == 'Y' and arr[i][1] < 37:
        cnt_arr[2] += 1
    elif arr[i][0] == 'N' and arr[i][1] < 37:
        cnt_arr[3] += 1

for i in range(len(cnt_arr)):
    print(f"{cnt_arr[i]}", end=' ')
if cnt_arr[0] >= 2:
    print("E")