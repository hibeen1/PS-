from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        tx, ty = q.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
    

t = int(input())
ans = []
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                cnt += 1
                # dfs(i, j)
                bfs(i, j)
    ans.append(cnt)
for i in ans:
    print(i)

