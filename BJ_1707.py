from collections import deque
import sys
input = sys.stdin.readline

def bfs(v, num):
    q = deque()
    q.append(v)
    visited[v] = num
    while q:
        temp = q.popleft()
        for i in graph[temp]:
            if visited[i] == 0:
                visited[i] = visited[temp] * (-1)
                q.append(i)
            elif visited[i] == visited[temp]:
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visited = [0 for _ in range(v)]
    for i in range(v):
        if not visited[i]:
            flag = bfs(i, 1)
            if not flag:
                break
    if 0 in visited:
        flag = False
    print("YES" if flag else "NO")