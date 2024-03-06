ns = input()
ms = input()

for i in range(len(ns)-len(ms)+1):
    flag = True
    for j in range(len(ms)):
        idx = i
        if ns[i+j] != ms[j]:
            flag = False
            idx = -1
        
    if flag:
        print(idx)
        break;

if idx == -1:
    print(-1)