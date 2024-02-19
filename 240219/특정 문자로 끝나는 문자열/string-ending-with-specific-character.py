arr = [
    input()
    for _ in range(10)
]
c = input()

flag = False
for str_ in arr:
    if str_[-1] == c:
        print(str_)
        flag = True

if flag == False:
    print("None")