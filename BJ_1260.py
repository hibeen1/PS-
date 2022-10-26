from collections import deque
import sys
input = sys.stdin.readline

def dfs(v, depth):
    print(v, end=" ")
    if depth == n:
        return
    for i in range(1, n+1):
        if adj_mat[v][i] and not visited[i]:
            visited[i] = True
            dfs(i, depth+1)

def bfs(v):
    q = deque()
    q.append(v)
    print(v, end=" ")
    while len(q) > 0:
        node = q.popleft()
        for i in range(1, n+1):
            if adj_mat[node][i] and not visited[i]:
                print(i, end=" ")
                visited[i] = True
                q.append(i)

n, m, v = map(int, input().split())
adj_mat = [[False for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj_mat[a][b] = True
    adj_mat[b][a] = True
visited = [False for _ in range(n+1)]
visited[v] = True
dfs(v, 1)
print()
visited = [False for _ in range(n+1)]
visited[v] = True
bfs(v)

