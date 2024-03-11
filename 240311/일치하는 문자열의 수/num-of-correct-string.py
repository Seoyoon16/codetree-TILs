n, s = input().split()
n = int(n)

cnt = 0
for _ in range(n):
    ss = input()
    flag = True
    if len(s) == len(ss):
        for i in range(len(ss)):
            if s[i] != ss[i]:
                flag = False

        if flag:
            cnt += 1

print(cnt)

# # Solution2
# #두 문자열이 동일한지 비교할 때도 == 연산자 사용

# for _ in range(n):
#     ss = input()
#     if s == ss:
#         cnt += 1