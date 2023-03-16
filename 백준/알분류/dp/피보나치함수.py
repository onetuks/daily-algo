# 1 0
# 0 1
# 1 2
# 5 8
# 10946 17711

file = open("피보나치함수.txt")

input = file.readline


dp = [[0, 0] for _ in range(41)]
dp[0], dp[1] = [1, 0], [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(*dp[n])


file.close()
