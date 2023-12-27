import sys

n1, n2 = tuple(map(int, input().split()))

arr_n1 = list(map(int, input().split()))
arr_n2 = list(map(int, input().split()))

for i in range(n1):
    success = True
    for j in range(n2):
        if i + j >= n1:
            success = False
            break;
        if arr_n1[i+j] != arr_n2[j]:
            success = False
            break
    if success:
        print("Yes")
        sys.exit()

print("No")