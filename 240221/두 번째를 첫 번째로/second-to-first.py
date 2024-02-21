s = list(input())

ch1 = s[1]
ch2 = s[0]
for i in range(len(s)):
    if s[i] == ch1:
        s[i] = ch2

for ch in s:
    print(ch, end='')