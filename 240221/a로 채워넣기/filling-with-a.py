# python에서 문자열은 immutable

s0 = input()
l = len(s0)

s1 = s0[0]
s2 = s0[2:l-2]
s3 = s0[-1]

print(s1 + 'a' + s2 + 'a' + s3)