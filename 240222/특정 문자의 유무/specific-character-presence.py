s = input()
a = "ee"
b = "ab"

flag_1 = False
flag_2 = False
for i in range(len(s)-2+1):
    for j in range(2):
        if s[i+j] == a[j]:
            flag_1 = True
        if  s[i+j] == b[j]:
            flag_2 = True

if flag_1:
    print("Yes", end=' ')
else :
    print("No", end=' ')

if flag_2:
    print("Yes")
else :
    print("No")