n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r][c] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end=' ')
    print()

# # How to search a particular point

# # the particular point that i try to search
# a, b = 1, 3

# # create a 10by10 2D array
# placed = [
#     [0 for _ in range(10)]
#     for _ in range(10)
# ]

# # mark given points
# for _ in range(3): # three is the number of points
#     r, c = tuple(map(int, input().split()))
#     placed[r][c] = 1

# # print the array
# for row in placed:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# print()

# # print result 
# exists = True if placed[a][b] == 1 else False
# print(exists)