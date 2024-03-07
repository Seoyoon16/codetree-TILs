s = input()
reqs = input()

for i in range(len(reqs)):
    if reqs[i] == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]

print(s)