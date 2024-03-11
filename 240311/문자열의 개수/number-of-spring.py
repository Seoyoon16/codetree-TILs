cnt = 0
ss = []
while (True):
    s = input()
    if s == '0': break

    cnt += 1

    if (cnt%2 != 0): ss.append(s)

print(cnt)
for elem in ss:
    print(elem)