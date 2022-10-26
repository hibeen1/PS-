import sys
input = sys.stdin.readline

n, k = map(int, input().split())
INF = int(1e9)
# dp[k][n]
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
for i in range(1, k+1):
    for j in range(1, n+1):
        if i == 1:
            dp[i][j] = j
            continue
        if i > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = INF
        for floor in range(1, j):
            temp = 1 + max(dp[i-1][floor-1], dp[i][j-floor])
            dp[i][j] = min(temp, dp[i][j])
print(dp[k][n])