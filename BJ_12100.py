import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
ans = -1e9

def union(li):
    idx = 0
    if len(li) > 1:
        while(True):
            if idx+1 >= len(li):
                break
            if li[idx] == li[idx+1]:
                li[idx] *= 2
                del li[idx+1]
            idx += 1
    return li

def up(graph):
    g = [[0] * n for _ in range(n)]
    for i in range(n):
        li = []
        for j in range(n):
            if graph[j][i] != 0:
                li.append(graph[j][i])
        if len(li) > 0:
            li = union(li)
            for j in range(len(li)):
                g[j][i] = li[j]
    return g

def down(graph):
    g = [[0] * n for _ in range(n)]
    for i in range(n):
        li = []
        for j in range(n-1, -1, -1):
            if graph[j][i] != 0:
                li.append(graph[j][i])
        if len(li) > 0:
            li = union(li)
            for j in range(len(li)):
                g[n-1-j][i] = li[j]
    return g

def west(graph):
    g = [[0] * n for _ in range(n)]
    for i in range(n):
        li = []
        for j in range(n):
            if graph[i][j] != 0:
                li.append(graph[i][j])
        if len(li) > 0:
            li = union(li)
            for j in range(len(li)):
                g[i][j] = li[j]
    return g

def east(graph):
    g = [[0] * n for _ in range(n)]
    for i in range(n):
        li = []
        for j in range(n-1, -1, -1):
            if graph[i][j] != 0:
                li.append(graph[i][j])
        if len(li) > 0:
            li = union(li)
            for j in range(len(li)):
                g[i][n-1-j] = li[j]
    return g

def play(depth, graph):
    if depth == 5:
        temp = -1
        for i in range(n):
            for j in range(n):
                temp = max(temp, graph[i][j])
        global ans
        ans = max(ans, temp)
        return
    play(depth+1, up([li[:] for li in graph]))
    play(depth+1, down([li[:] for li in graph]))
    play(depth+1, west([li[:] for li in graph]))
    play(depth+1, east([li[:] for li in graph]))

play(0, graph)
print(ans)

# # # # # tem = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # # # # tem[1][1] = tem[2][2]
# # # # # tem[2][2] = 100
# # # # # print(tem)

# li = [1, 1, 2, 2, 3, 4, 5, 5]  #len = 8
# for i in range(len(li) - 1):
#     print(i)
#     del li[0]
#     print(li)
#     # if i == len(li):
#     #     break
#     # print(li)
#     # if li[i] == li[i+1]:
#     #     li[i] *= 2
#     #     del li[i+1]
# print(li)

# 1 1 3     idx 0 len 3
# if li[0] == li[1]:
#     li[0] *= 2
#     del li[1]
# idx += 1

# 2 3     idx 1 len 2
# idx += 1

# 2 3     idx 2 len 2
