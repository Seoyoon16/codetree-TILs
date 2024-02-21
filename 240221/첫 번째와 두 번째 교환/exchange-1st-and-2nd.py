s = list(input())

ch1 = s[0]
ch2 = s[1]

for i in range(len(s)):
    if s[i] == ch1:
        s[i] = ch2
    elif s[i] == ch2:
        s[i] = ch1

for ch in s:
    print(ch, end='')