s1 = input()
s2 = input()

c1 = c2 = ''
for c in s1:
    if c.isdigit():
        c1 += c
for c in s2:
    if c.isdigit():
        c2 += c

print(int(c1) + int(c2))