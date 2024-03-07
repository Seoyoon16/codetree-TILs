# 대문자 to 소문자
# 1) 아스키 코드 활용 chr(ord(x)-n)
# 2) python lower 함수 활용 <-> upper()
#    형식: "string".lower()

# 문자열끼리의 비교
# 아스키 코드 번호 순으로 비교됨

# 알파벳 여부: isalpha()
# 숫자 여부: isdigit()
# 결과: Boolean
# 형식: "string".함수()

s = input()

for ch in s:
    if ch.isalpha():
        if ch >= 'A' and ch <= 'Z':
            print(ch, end='')
        else:
            print(chr(ord(ch) - 32), end='')