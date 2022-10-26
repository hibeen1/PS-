import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
v.insert(0, 0)
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 1:
            if j+v[i] <= m:
                dp[i][j+v[i]] = 1
            if j-v[i] >= 0:
                dp[i][j-v[i]] = 1
ans = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        ans = i
        break
print(ans)


# 재귀 : 실패
# n, s, m = map(int, input().split())
# v = list(map(int, input().split()))
# v.insert(0, 0)
# dp = [-1 for _ in range(n+1)]
# dp[0] = s
# cnt = 0
# def recur(depth, num):
#     global cnt
#     cnt+=1
#     if depth == n+1:
#         return
#     if num+v[depth] <= m:
#         dp[depth] = max(dp[depth], num+v[depth])
#         recur(depth+1, num+v[depth])
#     if num-v[depth] >= 0:
#         dp[depth] = max(dp[depth], num-v[depth])
#         recur(depth+1, num-v[depth])

# recur(1, dp[0])
# print(dp[n])