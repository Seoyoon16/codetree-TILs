s, c = input().split()

idx = 0
for i in range(len(s)):
    if s[i] == c:
        idx = i
        break;
    if c not in s:
        idx = -1

if idx == -1:
    print("No")
else: print(idx)