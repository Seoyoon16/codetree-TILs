s, q = input().split()
s = list(s)

for _ in range(int(q)):
    l = list(input().split())

    if l[0] == "1":
        ch1 = s[int(l[1])-1]
        ch2 = s[int(l[2])-1]
        s[int(l[1])-1] = ch2
        s[int(l[2])-1] = ch1
    elif l[0] == "2":
        ch1 = l[1]
        ch2 = l[2]
        for j in range(len(s)):
            if s[j] == ch1:
                s[j] = ch2
    
    for ch in s:
        print(ch, end='')
    print()