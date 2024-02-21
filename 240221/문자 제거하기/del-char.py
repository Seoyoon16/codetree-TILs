s = list(input())

num_l = [
    int(input())
    for _ in range(len(s)-1)
]

for i in range(len(num_l)):
    if num_l[i] >= len(s):
        s.pop(-1)
        res = ''.join(s)
        print(res)
    else:
        s.pop(num_l[i])
        res = ''.join(s)
        print(res)