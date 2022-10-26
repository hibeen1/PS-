# https://www.acmicpc.net/problem/7569

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(box):
    q = deque()
    for z in range(len(box)):
        for x in range(len(box[0])):
            for y in range(len(box[0][0])):
                if box[z][x][y] == 1:
                    q.append((z,x,y))
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append((nz, nx, ny))
    

def check(box):
    result = 0
    for z in range(len(box)):
        for x in range(len(box[0])):
            for y in range(len(box[0][0])):
                result = max(result, box[z][x][y])
                if box[z][x][y] == 0:
                    return -1
    return result-1
    


m, n, h = map(int, input().split())

box = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int, input().split())))
bfs(box)
print(check(box))


       
            
                