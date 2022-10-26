# https://www.acmicpc.net/problem/12865
# DP, Knapsack problem
# https://roamingman.tistory.com/62

import sys
input = sys.stdin.readline


# # 1차원 배열 풀이법
# n, k = map(int, input().split())
# dp = [0] * (k+1)
# for _ in range(n):
#     w, v = map(int, input().split())
#     if w > k:
#         continue
#     for j in range(k, 0, -1):
#         if j+w <= k and dp[j] != 0:
#             dp[j+w] = max(dp[j+w], dp[j] + v)
#     dp[w] = max(dp[w], v)

# print(max(dp))


# 2차원 배열 풀이법
n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[n][k])