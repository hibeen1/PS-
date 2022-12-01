import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N = int(input())
MIN = 101
MAX = 0
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    max_temp = max(graph[i])
    min_temp = min(graph[i])
    MAX = max(MAX, max_temp)
    MIN = max(MIN, min_temp)

ans = 0
for val in range(MIN, MAX+1):
    temp = deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if temp[i][j] <= val:
                temp[i][j] = 0

def bfs(x, y):
    q = deque()
    
