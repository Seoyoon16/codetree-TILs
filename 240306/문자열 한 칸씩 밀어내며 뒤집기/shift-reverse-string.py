s, q = input().split()
q = int(q)

reqs = [
    int(input())
    for _ in range(q)
]
# print(reqs)

for rq in reqs:
    if rq == 1:
        s = s[1:] + s[0]
        print(s)
    elif rq == 2:
        s = s[-1] + s[:-1]
        print(s)
    else:
        s = s[-1::-1]
        print(s)