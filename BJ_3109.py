import sys
input = sys.stdin.readline

def dfs(i, j):
    print("hello", i, j)
    if j == c-1:
        return True
    for x in dx:
        nx = i + x
        ny = j + 1
        if 0 <= nx < r and ny < c and graph[nx][ny] == "." and not visited[nx][ny]:
            visited[nx][ny] = True
            if dfs(nx, ny):
                return True
    return False

r, c = map(int, input().split())
graph = []
dx = [-1, 0, 1] # 순서 중요
for _ in range(r):
    graph.append(input().rstrip())
ans = 0
visited = [[False] * c for _ in range(r)]
for i in range(r):
    if graph[i][0] == ".":
        if dfs(i, 0):
            ans += 1
print(ans)