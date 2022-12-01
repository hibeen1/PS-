import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

def bfs(x, y, val):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if temp[nx][ny] <= 0:
                continue
            temp[nx][ny] = 0
    return 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
MIN = 101
MAX = 0
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    max_temp = max(graph[i])
    min_temp = min(graph[i])
    MAX = max(MAX, max_temp)
    MIN = min(MIN, min_temp)

ans = 0
for val in range(MIN, MAX+1):
    temp = deepcopy(graph)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if temp[i][j] <= val:
                temp[i][j] = 0
    for i in range(N):
        for j in range(N):
            cnt += bfs(i, j, val)
    print(cnt)
    ans = max(ans, cnt)

print(ans)


