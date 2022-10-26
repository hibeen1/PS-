from gettext import find
from sys import stdin
input = stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
pipes = ['|', '-', '+', '1', '2', '3', '4']


def find_endpoint(p, visited):
    flag = False
    for i in range(4):
        nx = p[0] + dx[i]
        ny = p[1] + dy[i]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if graph[nx][ny] != "." and not visited[nx][ny]:
                flag = True
                visited[nx][ny] = True
                tp = find_endpoint([nx, ny], visited)
    if not flag:
        return [nx, ny]
    else:
        return tp



r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(input().rstrip())

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'M':
            mp = [i, j]
        elif graph[i][j] == 'Z':
            zp = [i, j]
visited = [[False for _ in range(c)] for _ in range(r)]
visited[mp[0]][mp[1]] = True
print(mp)
print(zp)
print(find_endpoint(mp, visited))
visited = [[False for _ in range(c)] for _ in range(r)]
visited[zp[0]][zp[1]] = True
print(find_endpoint(zp, visited))