import sys
input = sys.stdin.readline
n = int(input())
cnt = 0

def pipe_move(state, x, y):
    if x == n-1 and y == n-1:
        global cnt
        cnt += 1
        return
    if state == 0:
        if y+1 < n:
            if graph[x][y+1] == 0:
                pipe_move(0, x, y+1)
                if x+1 < n:
                    if graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
                        pipe_move(2, x+1, y+1)
    elif state == 1:
        if x+1 < n:
            if graph[x+1][y] == 0:
                pipe_move(1, x+1, y)
                if y+1 < n:
                    if graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
                        pipe_move(2, x+1, y+1)
    elif state == 2:
        if y+1 < n:
            if graph[x][y+1] == 0:
                pipe_move(0, x, y+1)
        if x+1 < n:
            if graph[x+1][y] == 0:
                pipe_move(1, x+1, y)
        if x+1 < n and y+1 < n:                
            if graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
                pipe_move(2, x+1, y+1)
    else:
        return

# 가로 세로 대각선
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
pipe_move(0, 0, 1)
print(cnt)



# # 우 하 우하
# dx = [0, 1, 1]
# dy = [1, 0, 1]

# def h_possible(x, y):
#     nx = x + dx[0]
#     ny = y + dy[0]
#     if nx < n and ny < n:
#         if graph[nx][ny] == 0:
#             return True
#     return False

# def v_possible(x, y):
#     nx = x + dx[1]
#     ny = y + dy[1]
#     if nx < n and ny < n:
#         if graph[nx][ny] == 0:
#             return True
#     return False

# def c_possible(x, y):
#     for i in range(len(dx)):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= n or ny >= n:
#             return False
#         else:
#             if graph[nx][ny] != 0:
#                 return False
#     return True

# def dfs(head_x, head_y, state):
#     if head_x==n-1 and head_y==n-1:
#         global cnt
#         cnt += 1
#         return

#     if state == "cross":
#         if v_possible(head_x, head_y):
#             dfs(head_x+dx[1], head_y+dy[1], "vertical")
#         if h_possible(head_x, head_y):
#             dfs(head_x+dx[0], head_y+dy[0], "horizontal")
#         if c_possible(head_x, head_y):
#             dfs(head_x+dx[2], head_y+dy[2], "cross")

#     elif state == "horizontal":
#         if h_possible(head_x, head_y):
#             dfs(head_x+dx[0], head_y+dy[0], "horizontal")
#         if c_possible(head_x, head_y):
#             dfs(head_x+dx[2], head_y+dy[2], "cross")

#     elif state == "vertical":
#         if v_possible(head_x, head_y):
#             dfs(head_x+dx[1], head_y+dy[1], "vertical")
#         if c_possible(head_x, head_y):
#             dfs(head_x+dx[2], head_y+dy[2], "cross")

# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# dfs(0, 1, "horizontal")
# print(cnt)