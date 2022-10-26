# [제약 사항]

# 1. 7 ≤ N ≤ 12

# 2. Core의 개수는 최소 1개 이상 12개 이하이다.

# 3. 최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core가 존재할 수 있다.


# [입력]

# 입력의 가장 첫 줄에는 총 테스트 케이스의 개수 T가 주어지며 그 다음 줄부터 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 줄에는 N값이 주어지며,

# 다음 N줄에 걸쳐서 렉시노스의 초기 상태가 N x N 배열로 주어진다.

# 0은 빈 cell을 의미하며, 1은 core를 의미하고, 그 외의 숫자는 주어지지 않는다.


# [출력]

# 테스트 케이트의 결과는 '#X'를 찍고, 한 칸 띄고, 정답을 출력한다.

# (X는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 5
# 7
# 0 0 1 0 0 0 0
# 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0
# 1 1 0 1 0 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0
# 9
# 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0
# 0 0 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0 1
# 11
# 0 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 1
# 0 0 0 1 0 0 0 0 1 0 0
# 0 1 0 1 1 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0
# 12
# 0 0 0 0 0 1 1 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0 0 1 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 0 0 1 0
# 0 0 0 0 1 0 0 0 1 0 0 0
# 0 0 0 0 0 0 1 1 0 0 1 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 1
# 12
# 0 0 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 1 0 1 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 1 0 0 1 0 0
# 0 1 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0




dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(cur_idx, connected_num, line_cnt, visited):
    if cur_idx == len(cores):
        global connected
        global ans
        if connected_num >= connected:
            connected = connected_num
            ans = min(ans, line_cnt)
            return
    for i in range(4):
        x = cores[cur_idx][0]
        y = cores[cur_idx][1]
        flag = True
        points = []
        while True:
            x += dx[i]
            y += dy[i]
            if x < 0 or x >= n or y < 0 or y >= n:
                break
            points.append((x, y))
            if visited[x][y]:
                flag = False
                break
        if flag:
            for p in points:
                visited[p[0]][p[1]] = True
            dfs(cur_idx+1, connected_num+1, line_cnt+len(points), visited)
            for p in points:
                visited[p[0]][p[1]] = False


T = int(input())
answer = []
for t in range(1, T+1):
    n = int(input())
    graph = []
    cores = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                visited[i][j] = True
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    continue 
                cores.append((i, j))
    
    ans = 1e9
    connected = 0
    dfs(0, 0, 0, visited)
    answer.append("#" + str(t) + " " + str(ans))
for ans in answer:
    print(ans)