import sys
input = sys.stdin.readline

n = int(input())
graph = []
w_cnt = 0
b_cnt = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

def check(x, y, dist):
    flag = True
    for i in range(x, x+dist):
        for j in range(y, y+dist):
            if graph[i][j] != graph[x][y]:
                flag = False
                n_dist = int(dist/2)
                check(x, y, n_dist)
                check(x, y+n_dist, n_dist)
                check(x+n_dist, y, n_dist)
                check(x+n_dist, y+n_dist, n_dist)
                return
    if flag:
        global w_cnt
        global b_cnt
        if graph[x][y] == 0:
            w_cnt += 1
        else:
            b_cnt += 1

check(0, 0, n)
print(w_cnt)
print(b_cnt)
    