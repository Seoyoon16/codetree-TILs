arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]
sum_v = 0; k = 3
for i in range(4):
    for j in range(4):
        if i+j > 3:
            break;
        sum_v += arr_2d[j+i][i]

print(sum_v)



# 합
# for i in range(4):
# 	for j in range(i + 1):
# 		sum_val += arr_2d[i][j]