import sys

n = int(input())
arr = list(map(int, input().split()))

idx = n
while True:
    vmax = -sys.maxsize
    for elem in (arr[:idx]):
        if elem >= vmax:
            vmax = elem
    idx = arr.index(vmax)
    print(idx+1, end=' ')
    if idx == 0:
        break;