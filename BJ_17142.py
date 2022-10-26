from collections import deque
import sys
from itertools import combinations
input = sys.stdin.readline
min_time = 1e9
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class virus:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def zero_count(graph):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                cnt += 1;
    return cnt
    

def bfs(v_list, cnt):
    global min_time
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    for i in v_list:
        q.append(i)
    time = 0
    while True:
        q_size = len(q)
        if cnt == 0:
            min_time = min(min_time, time)
            break
        if time >= min_time:
            break 
        if q_size == 0:
            if cnt == 0:
                min_time = min(min_time, time)
            break

        for _ in range(q_size):
            v = q.popleft()
            for i in range(4):
                nx = v.x + dx[i]
                ny = v.y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if graph[nx][ny] != 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append(virus(nx, ny))
                        if graph[nx][ny] == 0:
                            cnt -= 1
        time+=1
        
n, m = map(int, input().split())
graph = []
v_list = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            v_list.append(virus(i, j))
if zero_count(graph) == 0:
    print(0)
else:    
    v_combi_list = list(combinations(v_list, m))
    zero = zero_count(graph)
    for i in v_combi_list:
        bfs(i, zero)
    if min_time == 1e9:
        min_time = -1
    print(min_time)