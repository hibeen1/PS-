# https://www.acmicpc.net/problem/14500
# 구현, 브루트포스

import sys
input = sys.stdin.readline

def make_tetromino(x, y):
    li = []
    # 긴 작대기
    if y+3 < m:
        li.append([(x, y), (x, y+1), (x, y+2), (x, y+3)])
    if x+3 < n:
        li.append([(x, y), (x+1, y), (x+2, y), (x+3, y)])
    # 정사각형
    if x+1 < n and y+1 < m:
        li.append([(x, y), (x+1, y), (x, y+1), (x+1, y+1)])
    
    if x+2 < n and y+1 < m:
        # 기역니은
        li.append([(x, y), (x+1, y), (x+2, y), (x+2, y+1)])
        li.append([(x, y+1), (x+1, y+1), (x+2, y+1), (x+2, y)])
        li.append([(x, y), (x, y+1), (x+1, y), (x+2, y)])
        li.append([(x, y), (x, y+1), (x+1, y+1), (x+2, y+1)])

        # 계단
        li.append([(x, y), (x+1, y), (x+1, y+1), (x+2, y+1)])
        li.append([(x, y+1), (x+1, y), (x+1, y+1), (x+2, y)])
        
        # 뻐큐모양
        li.append([(x, y), (x+1, y), (x+2, y), (x+1, y+1)])
        li.append([(x, y+1), (x+1, y+1), (x+2, y+1), (x+1, y)])

    if x+1 < n and y+2 < m:
        li.append([(x, y), (x+1, y), (x, y+1), (x, y+2)])
        li.append([(x, y), (x+1, y), (x+1, y+1), (x+1, y+2)])
        li.append([(x, y), (x, y+1), (x, y+2), (x+1, y+2)])
        li.append([(x+1, y), (x+1, y+1), (x+1, y+2), (x, y+2)])

        li.append([(x, y), (x, y+1), (x+1, y+1), (x+1, y+2)])
        li.append([(x+1, y), (x+1, y+1), (x, y+1), (x, y+2)])

        li.append([(x+1, y), (x+1, y+1), (x+1, y+2), (x, y+1)])
        li.append([(x, y), (x, y+1), (x, y+2), (x+1, y+1)])
    return li




n, m = map(int, input().split())
graph = []
ans = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
for x in range(n):
    for y in range(m):
        li = make_tetromino(x, y)
        for c in li:
            temp = 0
            for i in range(4):
                temp += graph[c[i][0]][c[i][1]]
            ans = max(ans, temp)
print(ans)
