# 하나의 문자열의 쓰임은 마치 1차원 배열과 같고, 문자열 리스트의 경우에는 마치 2차원 배열과 같이 동작
a = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]

cnt = 0
for str_ in arr:
    if a == str_[2] or a == str_[3]:
        cnt += 1
        print(str_)
print(cnt)