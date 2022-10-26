from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = []
rx, ry, bx, by = -1, -1, -1, -1
for i in range(n):
    graph.append(input().rstrip())
    for j in range(m):
        if graph[i][j] == "R":
            rx, ry = i, j
        if graph[i][j] == "B":
            bx, by = i, j

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    cnt = 0
    while q:
        for _ in range(len(q)):
            if cnt > 10:
                print(-1)
                return
            rx, ry, bx, by = q.popleft()
            if graph[rx][ry] == "O":
                print(cnt)
                return
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == "#" or (nrx < 0 or nrx >= n or nry < 0 or nry >= m):
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == "O":
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == "#" or (nbx < 0 or nbx >= n or nby < 0 or nby >= m):
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == "O":
                        break
                if graph[nbx][nby] == "O":
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx-rx)+abs(nry-ry) < abs(nbx-bx)+abs(nby-by):
                        nbx -= dx[i]
                        nby -= dy[i]
                    else:
                        nrx -= dx[i]
                        nry -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    visited.append((nrx, nry, nbx, nby))
                    q.append(visited[-1])
        cnt += 1
    print(-1)

bfs(rx, ry, bx, by)