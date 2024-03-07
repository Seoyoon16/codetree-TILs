n1, n2 = input().split()

n = int(n1) + int(n2)
n = str(n)

cnt = 0
for num in n:
    if num == '1':
        cnt += 1
print(cnt)