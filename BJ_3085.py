import sys
input = sys.stdin.readline
# 하 우
dx = [1, 0]
dy = [0, 1]

def check(n, graph):
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if graph[i][j] == graph[i][j-1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        if cnt != 1:
            max_cnt = max(max_cnt, cnt)
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if graph[j][i] == graph[j-1][i]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        if cnt != 1:
            max_cnt = max(max_cnt, cnt)
    return max_cnt

n = int(input())
graph = []
answer = -1
for _ in range(n):
    graph.append(list(map(str, " ".join(input()).split())))
for x in range(n):
    for y in range(n):
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] != graph[x][y]:
                    graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                    answer = max(answer, check(n, graph))
                    graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
print(answer)


