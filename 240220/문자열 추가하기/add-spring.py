# 문자열 concat
# 1) 문자열끼리의 + 연산
# 2) 새로운 문자열을 선언하여 ""로 초기화 후 더해주기
# a, b, c = "apple", "banana", "candy"
# tot_str = ""
# for target_str in [a, b, c]:
#     tot_str += target_str
# 3) join() 함수를 이용하여 여러 문자열을 하나로 합치기
# 구분값.join(리스트) ---> tot_str = "".join([a, b, c])

s = input()
s += "Hello"
print(s)