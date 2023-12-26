# # 1
# word = ['A', 'P', 'P', 'L', 'E']

# # 해당 문자를 찾지 못했다면 -1
# idx = -1

# # 문자 탐색
# for i, char in enumerate(word):
#     if char == 'L':
#         idx = i

# # 문자가 존재하지 않는 경우
# if idx == -1:
#     print("not exist")
# else:
#     print(idx)

# # 2
# word = ['A', 'P', 'P', 'L', 'E']
# print(word.index('L'))

arr = ['L', 'E', 'B', 'R', 'O', 'S']
letter = input()

for i, char in enumerate(arr):
    if char == letter:
        print(i)
if letter not in arr:
        print("None")