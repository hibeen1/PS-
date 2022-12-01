# https://www.acmicpc.net/problem/9466
# https://deep-learning-study.tistory.com/583
# dfs, 그래프

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x):
    global teams
    visited[x] = True
    temp.append(x)
    next = graph[x]
    if visited[next]:
        if next in temp:
            teams += temp[temp.index(next):]
    else:
        dfs(next)


t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [True] + [False for _ in range(n)]
    teams = []
    for i in range(1, n+1):
        if not visited[i]:
            temp = []
            dfs(i)
    ans.append(n-len(teams))
for i in ans:
    print(i)