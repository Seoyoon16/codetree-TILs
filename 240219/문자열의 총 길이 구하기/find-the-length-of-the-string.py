# 공백 단위로 정확히 2개의 문자열을 입력 받을때는 굳이 map 함수를 사용하지 않고 tuple만 사용하여 쉽게 구현

arr = input().split()

cnt = 0
for str_ in arr:
    cnt += len(str_)

print(cnt)