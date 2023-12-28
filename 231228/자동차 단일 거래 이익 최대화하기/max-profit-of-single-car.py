n = int(input())
price = list(map(int, input().split()))

max_profit = 0     # 이익관점에서 접근
for i in range(n):
    for j in range(i+1, n):
        profit = price[j] - price[i]

        if profit > max_profit:
            max_profit = profit

print(max_profit)