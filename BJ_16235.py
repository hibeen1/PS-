# 상 하 좌 우 상우 상좌 하우 하좌
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

n, m, k = map(int, input().split())
A_list = []
tree_graph = [[[] for _ in range(n)] for _ in range(n)]
soil_graph = [[5 for _ in range(n)] for _ in range(n)]
for i in range(n):
    A_list.append(list(map(int, input().split())))
    for j in range(n):
        soil_graph[i][j] += A_list[i][j]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree_graph[x-1][y-1].append(z)
for tc in range(k):
    # 봄, 여름
    for i in range(n):
        for j in range(n):
            if len(tree_graph[i][j]) == 0:
                continue
            else:
                tree_graph[i][j] = sorted(tree_graph[i][j])
                dead_tree = 0
                remove_list = []
                for idx in range(len(tree_graph[i][j])):
                    if soil_graph[i][j] >= tree_graph[i][j][idx]:
                        soil_graph[i][j] -= tree_graph[i][j][idx]
                        tree_graph[i][j][idx] += 1
                    else:
                        dead_tree += int(tree_graph[i][j][idx]/2)
                        remove_list.append(idx)
                remove_list.sort(reverse=True)
                if len(remove_list) > 0:
                    for idx in remove_list:
                        del tree_graph[i][j][idx]
                soil_graph[i][j] += dead_tree
# 가을, 겨울
    for i in range(n):
        for j in range(n):
            if len(tree_graph[i][j]) == 0:
                continue
            for tree in tree_graph[i][j]:
                if tree % 5 == 0:
                    for t in range(8):
                        nx = i + dx[t]
                        ny = j + dy[t]
                        if nx >= 0 and nx < n and ny >= 0 and ny < n:
                            tree_graph[nx][ny].append(1)
            soil_graph[i][j] += A_list[i][j]
    for i in range(n):
        for j in range(n):
            print(len(tree_graph[i][j]), end=" ")
        print(end="\t\t")
        for j in range(n):
            print(soil_graph[i][j], end=" ")
        print()
    print()
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree_graph[i][j])
print(answer)