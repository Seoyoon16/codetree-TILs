n = int(input())

arr = [
    input()
    for _ in range(n)
]

leng = 0; cnt =0
for elem in arr:
    leng += len(elem)
    if elem[0] == 'a':
        cnt += 1

print(leng, cnt)