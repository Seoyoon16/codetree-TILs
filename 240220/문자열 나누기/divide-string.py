n = int(input())
nums = input().split()

ts = ""
for s in nums:
    ts += s

for i in range(0, len(ts), 5):
    print(ts[i:i+5]) 

# for i in range(leng):
# 	print(str_all[i], end="")
# 	if (i + 1) % 5 == 0:
# 		print()