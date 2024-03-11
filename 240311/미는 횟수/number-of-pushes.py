A = input()
B = input()

n = 0
for i in range(len(A)):
    A = A[-1] + A[:-1]
    n += 1
    if B == A: break;
    if n == len(A): n = -1

print(n)