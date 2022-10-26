# 위상정렬
# https://www.acmicpc.net/problem/2252

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
order = [[] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    order[a].append(b)
    depth[b] += 1

q = deque()

for i in range(1, n+1):
    if depth[i] == 0:
        q.append(i)

answer = []
while q:
    num = q.popleft()
    answer.append(str(num))
    for i in order[num]:
        depth[i] -= 1
        if depth[i] == 0:
            q.append(i)
print(" ".join(answer))
    
        