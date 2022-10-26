from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [0] * 100001

def bfs(n):
    q = deque()
    cnt = 0
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for i in ([x-1, x+1, x*2]):
            if i >= 0 and i <= 100000 and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)
bfs(n)