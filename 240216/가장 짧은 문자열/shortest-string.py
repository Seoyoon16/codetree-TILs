input_1 = input()
input_2 = input()
input_3 = input()

a = len(input_1)
b = len(input_2)
c = len(input_3)

max = min = 0
if a > b:
    if a > c:
        max = a
    else:
        max = c
    
    if b > c:
        min = c
    else:
        min = b
else:
    if b > c:
        max = b
    else:
        max = c
    
    if a > c:
        min = c
    else:
        min = a

print(max - min)