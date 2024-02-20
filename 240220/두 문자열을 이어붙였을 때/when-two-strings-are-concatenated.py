s1 = input()
s2 = input()

ts1 = ""; ts2 = ""
ts1 = s1 + s2
ts2 = s2 + s1

if ts1 == ts2:
    print("true")
else: print("false")