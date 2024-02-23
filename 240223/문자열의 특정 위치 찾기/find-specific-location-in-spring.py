s, c = input().split()

idx = 0
for i in range(len(s)):
    if s[i] == c:
        idx = i
        break;

if idx == 0:
    idx = "No"

print(idx)