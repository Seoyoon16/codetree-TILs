n = int(input())
arr = [
    input()
    for _ in range(n)
]
c = input()

leng = 0; cnt = 0
for str_ in arr:
    if str_[0] == c:
        leng += len(str_)
        cnt += 1

avg = leng / cnt
print(f"{cnt} {avg:.2f}")