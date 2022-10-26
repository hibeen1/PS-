from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs(coordinate):
    q = deque()
    q.append(coordinate)
    cnt = 1
    graph[coordinate[0]][coordinate[1]] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))
    return cnt

graph = []
ans = []
n = int(input())
for _ in range(n):
    graph.append(list(map(int, ' '.join(input()).split())))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs((i, j)))
print(len(ans))
ans.sort()
for i in ans:
    print(i)