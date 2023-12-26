a, b = tuple(map(int, input().split()))

cnt_arr = [0] * 10

while True:
    if a <= 1:
        break;
    
    elem = a % b
    cnt_arr[elem] += 1
    a = a // b

sum_v = 0
for i in range(len(cnt_arr)):
    sum_v += cnt_arr[i] ** 2
print(sum_v)