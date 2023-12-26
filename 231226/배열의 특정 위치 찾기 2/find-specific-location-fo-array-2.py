arr = list(map(int, input().split()))

sum_e=0; sum_o=0
for i in range(len(arr)):
    if i%2 == 0:
        sum_o += arr[i]
    else: sum_e += arr[i]

if sum_e >= sum_o:
    print(sum_e-sum_o)
else: print(sum_o-sum_e)