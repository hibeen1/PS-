# 위상정렬
# https://www.acmicpc.net/problem/1005


# import sys
# input = sys.stdin.readline

# def find_dp(num):
#     li = []
#     for i in order[num]:
#         if dp[i] != -1:
#             dp[i] = find_dp(i)
#         li.append(dp[i])
#     if len(li) == 0:
#         return d[num-1]
#     return d[num-1] + max(li)


# t = int(input())
# answers = []

# for _ in range(t):
#     n, k = map(int, input().split())
#     d = list(map(int, input().split()))
#     order = [[] for _ in range(n+1)]
#     dp = [-1 for _ in range(n+1)]
#     for i in range(1, n+1):
#         if len(order[i]) == 0:
#             dp[i] = d[i-1]

#     for _ in range(k):
#         x, y = map(int, input().split())
#         order[y].append(x)
#     w = int(input())
#     answers.append(find_dp(w))

# for answer in answers:
#     print(answer)
    

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
answers = []

for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    order = [[] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    depth = [0 for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split())
        order[x].append(y)
        depth[y] += 1
    w = int(input())

    q = deque()
    for i in range(1, n+1):
        if depth[i] == 0:
            dp[i] = d[i]
            q.append(i)
    while q:
        num = q.popleft()
        for i in order[num]:
            depth[i] -= 1
            dp[i] = max(dp[num] + d[i], dp[i])
            if depth[i] == 0:
                q.append(i)
    answers.append(dp[w])

for answer in answers:
    print(answer)