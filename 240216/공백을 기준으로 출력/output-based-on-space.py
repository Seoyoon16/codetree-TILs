input1 = input()
input2 = input()

input_ = (input1 + input2).replace(' ', '')
print(input_)

# 방법
# 1) 결과문자열 = 문자열.replace(old, new)
# 2) 문자열을 전부 순회하며 공백을 제외한 모든 문자를 출력
#   for elem in string:
# 	    if elem != " ":
# 		    print(elem, end="")
#   for elem in string2:
# 	    if elem != " ":
# 		    print(elem, end="")