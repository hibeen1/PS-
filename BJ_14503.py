# https://www.acmicpc.net/problem/14503
# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def get_idx(d):
    if d == 0:
        return 3
    return d-1

def vacuum(r, c, d):
    graph[r][c] = 2
    cnt = 1
    while True:
        is_vacuumed = False
        for _ in range(4):
            d = get_idx(d)
            nr = r + dx[d]
            nc = c + dy[d]
            #　범위를 벗어난 경우
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            # 이미　깨끗한　경우 or 벽인 경우
            if graph[nr][nc] != 0:
                continue
            graph[nr][nc] = 2
            cnt += 1
            r, c = nr, nc
            is_vacuumed = True
            break
        if not is_vacuumed:
            nr = r - dx[d]
            nc = c - dy[d]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                break
            if graph[nr][nc] == 1:
                break
            r, c = nr, nc
    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
print(vacuum(r, c, d))