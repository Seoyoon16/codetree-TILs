# new_arr = [elem * 2 for elem in arr if elem%2 == 0]
# list_ = [(i + j) for i in range(3) for j in range(3)]

n = int(input())
arr = list(map(int, input().split()))

arr_pow = [elem ** 2 for elem in arr]
for num in arr_pow:
    print(num, end=' ')