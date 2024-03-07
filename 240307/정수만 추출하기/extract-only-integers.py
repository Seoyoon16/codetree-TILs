s1, s2 = input().split()

z1 = z2 = ''
for ch1 in s1:
    if ch1.isdigit() != True:
        break;
    z1 += ch1

for ch2 in s2:
    if ch2.isdigit() != True:
        break;
    z2 += ch2

print(int(z1)+int(z2))