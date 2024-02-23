s = input()

a = "ee"
b = "ab"
flag1 = False
flag2 = False

for i in range(len(s)-2+1):
    if s[i] == a[0] and s[i+1] == a[1]:
        flag1 = True
    if s[i] == b[0] and s[i+1] == b[1]:
        flag2 = True

if flag1 == True:
    print("Yes", end=' ')
else:
    print("No", end=' ')

if flag2 == True:
    print("Yes", end=' ')
else:
    print("No", end=' ')