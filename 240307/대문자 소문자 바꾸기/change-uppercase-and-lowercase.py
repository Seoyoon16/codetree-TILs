s = input()

for ch in s:
    if ch >= 'A' and ch <= 'Z':
        print(chr(ord(ch)+32), end='')
    elif ch >= 'a' and ch <= 'z':
        print(chr(ord(ch)-32), end='')