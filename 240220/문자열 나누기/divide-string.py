n = int(input())
nums = input().split()

ts = ""
for s in nums:
    ts += s

for i in range(0, len(ts), 5):
    print(ts[i:i+5])