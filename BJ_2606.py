from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
edge = int(input())
computers = [[] for _ in range(n+1)]
for _ in range(edge):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

q = deque()
q.append(1)
ans = 0
visited = [False for _ in range(n+1)]
visited[1] = True
while q:
    idx = q.popleft()
    for i in computers[idx]:
        if not visited[i]:
            visited[i] = True
            ans += 1
            q.append(i)
print(ans)