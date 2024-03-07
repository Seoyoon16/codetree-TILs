s = input()

for elem in s:
    if elem.isdigit() or elem.isalpha():
        if elem >= 'A' and elem <= 'Z':
            print(chr(ord(elem)+32), end='')
        else:
            print(elem, end='')