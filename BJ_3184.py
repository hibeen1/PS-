from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global lamb, wolf
    if x < 0 or x >= r or y < 0 or y >= c:
        return False
    if visited[x][y]:
        return False
    if graph[x][y] == '#':
        return False
    else:
        if graph[x][y] == 'o':
            lamb += 1
        if graph[x][y] == 'v':
            wolf += 1
        graph[x][y] = '.'
        visited[x][y] = True
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

def bfs(i, j):
    q = deque()
    global lamb, wolf
    visited[i][j] = True
    if graph[i][j] == 'o':
        lamb += 1
    elif graph[i][j] == 'v':
        wolf += 1
    q.append([i, j])
    while len(q) > 0:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny] == '#':
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 'o':
                    lamb += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1
                graph[nx][ny] = '.'
                q.append([nx, ny])
    
r, c = map(int, input().split())
visited = [[False for _ in range(c)] for _ in range(r)]
graph = []
for _ in range(r):
    graph.append(list(input().strip()))
lambs, wolfs = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            lamb, wolf = 0, 0
            if dfs(i, j):
                if lamb > wolf:
                    lambs += lamb
                else:
                    wolfs += wolf
            # bfs(i, j)
            # if lamb > wolf:
            #     lambs += lamb
            # else:
            #     wolfs += wolf

print(lambs, wolfs)