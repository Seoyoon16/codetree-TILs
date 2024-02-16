input_1, input_2 = input().split()

if len(input_1) > len(input_2):
    print(input_1, len(input_1))
elif len(input_1) < len(input_2):
    print(input_2, len(input_2))
else:
    print("same")