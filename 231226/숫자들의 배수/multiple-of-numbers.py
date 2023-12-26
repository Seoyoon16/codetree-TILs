num = int(input())

arr = []; i = 1; cnt = 0
while True:
    arr.append(num*i)
    if num*i%5 == 0:
        cnt += 1
        if cnt == 2:
            break;
    i += 1
for num in arr:
    print(num, end=' ')