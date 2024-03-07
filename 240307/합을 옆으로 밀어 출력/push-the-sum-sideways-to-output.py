n = int(input())

ttl = 0
for _ in range(n):
    num = int(input())
    ttl += num

ttl = str(ttl)
ttl = ttl[1:] + ttl[0]
print(ttl)