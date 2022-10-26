import sys
input = sys.stdin.readline
cnt = 0
def recursive(x, y, depth):
    if depth > k:
        return
    if x < 0 or x >= r or y < 0 or y >= c or visited[x][y] or graph[x][y] == 'T':
        return
    if x == 0 and y == c-1:
        if depth == k:
            global cnt
            cnt += 1
        return
    visited[x][y] = True
    recursive(x+1, y, depth+1)
    recursive(x-1, y, depth+1)
    recursive(x, y+1, depth+1)
    recursive(x, y-1, depth+1)
    visited[x][y] = False
    
r, c, k = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input().strip()))
visited = [[False for _ in range(c)] for _ in range(r)]
recursive(r-1, 0, 1)
print(cnt)