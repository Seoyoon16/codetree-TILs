s = input()

res = 0
for elem in s:
    if elem.isdigit():
        res += int(elem)

print(res)