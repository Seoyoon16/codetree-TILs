input_ = list(input())
c = input()

cnt = 0
for i in range(len(input_)):
    if input_[i] == c:
        cnt += 1

print(cnt)