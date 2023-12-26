# n, q = tuple(map(int, input().split()))
# arr_n = list(map(int, input().split()))
# arr_q = []
# for i in range(q):
#     arr = list(map(int, input().split()))
#     arr_q.append(arr)

# for i in range(len(arr_q)):
#     if arr_q[i][0] == 1:
#         a = arr_q[i][1]
#         print(arr_n[a-1])
#     elif arr_q[i][0] == 2:
#         a = arr_q[i][1]
#         if a in arr_n:
#             idx = arr_n.index(a)
#             print(idx+1)            
#         else: print('0')
#     else:
#         a = arr_q[i][1]; b = arr_q[i][2]
#         for i in range(a-1, b):
#             print(arr_n[i], end=' ')
#         print()


n, q = tuple(map(int, input().split()))
arr_n = list(map(int, input().split()))

for i in range(q):
    arr_q = list(map(int, input().split()))

    if arr_q[0] == 1:
        a = arr_q[1]
        print(arr_n[a-1])
    elif arr_q[0] == 2:
        a = arr_q[1]
        if a in arr_n:
            idx = arr_n.index(a)
            print(idx+1)            
        else: print('0')
    else:
        a = arr_q[1]; b = arr_q[2]
        for i in range(a-1, b):
            print(arr_n[i], end=' ')
        print()