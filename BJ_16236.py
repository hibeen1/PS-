from collections import deque
import heapq
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    depth = 0
    graph[x][y] = 0
    q = deque()
    q.append([x, y])
    visited = [[False for _ in range(n)] for _ in range(n)]
    while q:
        depth += 1
        candi = []
        sz = len(q)
        print(q, depth)
        for _ in range(sz):
            cur = q.popleft()
            visited[cur[0]][cur[1]] = True
            for i in range(4):
                nx = cur[0] + dx[i]
                ny = cur[1] + dy[i]
                if nx >= n or nx < 0 or ny >= n or ny < 0:
                    continue
                if not visited[nx][ny] and graph[nx][ny] <= level:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    if graph[nx][ny] < level and graph[nx][ny] != 0:
                        candi.append([nx, ny])
        if len(candi) > 0:
            print("candi : ", candi, depth+1)
            return False, heapq.heappop(candi), depth+1
    return True, [x, y], depth


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            s_p = [i, j]
            graph[i][j] = 0
level = 2
feed = level
MAX = 1e9
time = 0

while True:
    is_finished, s_p, depth = bfs(s_p[0], s_p[1])
    print()
    if is_finished:
        print(time)
        break
    time += depth
    feed -= 1
    if feed == 0:
        level += 1
        feed = level

    



